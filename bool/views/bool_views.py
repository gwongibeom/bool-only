from flask import Blueprint, render_template

from bool.models import Bool

bp = Blueprint('bool', __name__, url_prefix='/bool')


@bp.route('/list/')
def _list():
    bool_list = Bool.query.order_by(Bool.create_date.desc())
    return render_template('bool/bool_list.html', bool_list=bool_list)


@bp.route('/detail/<int:bool_id>/')
def detail(bool_id):
    bool = Bool.query.get_or_404(bool_id)
    return render_template('bool/bool_detail.html', bool=bool)
