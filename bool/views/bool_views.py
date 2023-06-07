import os
from datetime import datetime
from flask import Blueprint, render_template, request, url_for, g, flash, jsonify
from werkzeug.utils import redirect
from ..filter import format_datetime
from .. import db
from bool.models import Bool
from bool.forms import BoolForm, CommentForm
from bool.views.auth_views import login_required
from sqlalchemy import func

bp = Blueprint('bool', __name__, url_prefix='/bool')


@bp.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    return response


@bp.route('/list/<string:cate>')
@bp.route('/list/')
def _list(cate=None):
    if cate:
        bool_list = Bool.query.filter_by(cate=cate).order_by(Bool.create_date.desc())
    else:
        bool_list = Bool.query.order_by(Bool.create_date.desc())
    return render_template('bool/index.html', bool_list=bool_list)


@bp.route('/detail/<int:bool_id>/')
def detail(bool_id):
    form = CommentForm()
    bool = Bool.query.get_or_404(bool_id)
    return render_template('bool/bool_detail.html', bool=bool, form=form)


@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = BoolForm()
    if request.method == 'POST' and form.validate_on_submit():
        bool = Bool(subject=form.subject.data, content=form.content.data, create_date=datetime.now(), user=g.user,
                    cate=form.category.data)
        db.session.add(bool)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('bool/bool_form.html', form=form)


@bp.route('/vote_good/<int:bool_id>/')
@login_required
def vote_good(bool_id):
    _bool = Bool.query.get_or_404(bool_id)
    if g.user == _bool.user:
        flash('본인이 작성한 글은 추천할수 없습니다')
    else:
        _bool.voter_good.append(g.user)
        db.session.commit()
    return redirect(url_for('bool.detail', bool_id=bool_id))


@bp.route('/vote_bad/<int:bool_id>/')
@login_required
def vote_bad(bool_id):
    _bool = Bool.query.get_or_404(bool_id)
    if g.user == _bool.user:
        flash('본인이 작성한 글은 비추천할수 없습니다')
    else:
        _bool.voter_bad.append(g.user)
        db.session.commit()
    return redirect(url_for('bool.detail', bool_id=bool_id))


@bp.route('/api/best')
def bool_best():
    bool_list = Bool.query.join(Bool.voter_good).group_by(Bool.id).order_by(func.count().desc()).all()
    result = []
    for bool in bool_list:
        result.append({
            'id': bool.id,
            'subject': bool.subject,
            'cate': bool.cate,
            'user': bool.user.username,
            'content': bool.content,
            'date': format_datetime(bool.create_date),
            'good_votes': len(bool.voter_good),
            'bad_votes': len(bool.voter_bad),
        })
    return jsonify(result)
