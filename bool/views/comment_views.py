from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from bool import db
from bool.models import Bool, Comment

bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/create/<int:bool_id>', methods=('POST',))
def create(bool_id):
    _bool = Bool.query.get_or_404(bool_id)
    content = request.form['content']
    comment = Comment(content=content, create_date=datetime.now())
    _bool.Comment_set.append(comment)
    db.session.commit()
    return redirect(url_for('bool.detail', bool_id=bool_id))