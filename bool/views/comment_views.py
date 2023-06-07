from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g
from werkzeug.utils import redirect
from bool.views.auth_views import login_required
from bool import db
from ..forms import CommentForm
from bool.models import Bool, Comment

bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/create/<int:bool_id>', methods=('POST',))
@login_required
def create(bool_id):
    form = CommentForm()
    bool = Bool.query.get_or_404(bool_id)
    if form.validate_on_submit():
        content = request.form['content']
        comment = Comment(content=content, create_date=datetime.now(), user=g.user)
        bool.Comment_set.append(comment)
        db.session.commit()
        return redirect(url_for('bool.detail', bool_id=bool_id))
    return render_template('bool/bool_detail.html', bool=bool, form=form)
