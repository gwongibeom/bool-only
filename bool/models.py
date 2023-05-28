from bool import db


class Bool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bool_id = db.Column(db.Integer, db.ForeignKey('bool.id', ondelete='CASCADE'))
    bool = db.relationship('Bool', backref=db.backref('Comment_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
