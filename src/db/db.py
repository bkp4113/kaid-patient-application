from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'sqlite:////home/bhaumik/kaid-patient-application/kaid_app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

db.engine.table_names()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    passwd = db.Column(db.String(128))
    #posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roles = db.Column(db.String(10))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

u = User(username="Bob")
db.session.
db.session.commit()



class Patient(Model):
    __tablename__ = 'paitent'
    id = Column('paitent_id', Integer, primary_key=True)
    first_name = Column('first_name', String(200))
    middle_name = Column('first_name', String(200))
    last_name = Column('first_name', String(200))
    dob = Column('first_name', String(10))
    gender = Column('first_name', String(10))

    def __init__(self, first_name, middle_name, last_name, dob, gender):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender

    def to_json(self):
        return dict(name=self.first_name, is_admin=self.is_admin)

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

# class User(Model):
#     __tablename__ = 'users'
#     id = Column('user_id', Integer, primary_key=True)
#     openid = Column('openid', String(200))
#     name = Column(String(200))

#     def __init__(self, name, openid):
#         self.name = name
#         self.openid = openid

#     def to_json(self):
#         return dict(name=self.name, is_admin=self.is_admin)

#     @property
#     def is_admin(self):
#         return self.openid in app.config['ADMINS']

#     def __eq__(self, other):
#         return type(self) is type(other) and self.id == other.id

#     def __ne__(self, other):
#         return not self.__eq__(other)

