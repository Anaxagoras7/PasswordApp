from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String)
    file = db.Column(db.String)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(50), unique=True)
    password = db.Column(db.String)
    
    def __repr__(self):
        return '<Task %r>' % self.id