from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect

from bool.models import Comment, Bool
from .. import db

bp = Blueprint('profile', __name__, url_prefix='/profile/')

from sqlalchemy import func


@bp.route('<int:user_id>')
def profile(user_id):
    user_id = user_id
    comment_count = db.session.query(func.count(Comment.id)).filter(Comment.user_id == user_id).scalar()
    bool_count = db.session.query(func.count(Bool.id)).filter(Bool.user_id == user_id).scalar()

    return render_template('profile/profile.html', comment_count=comment_count, bool_count=bool_count, user_id=user_id)
