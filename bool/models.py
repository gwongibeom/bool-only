from bool import db

bool_good_voter = db.Table(
    'bool_good_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('bool_id', db.Integer, db.ForeignKey('bool.id', ondelete='CASCADE'), primary_key=True)
)

bool_bad_voter = db.Table(
    'bool_bad_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('bool_id', db.Integer, db.ForeignKey('bool.id', ondelete='CASCADE'), primary_key=True)
)


class Bool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('Bool_set'))
    cate = db.Column(db.Text(), nullable=False)
    voter_good = db.relationship('User', secondary=bool_good_voter, backref=db.backref('bool_good_voter_set'))
    voter_bad = db.relationship('User', secondary=bool_bad_voter, backref=db.backref('bool_bad_voter_set'))


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bool_id = db.Column(db.Integer, db.ForeignKey('bool.id', ondelete='CASCADE'))
    bool = db.relationship('Bool', backref=db.backref('Comment_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('Comment_set'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
