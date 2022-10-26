from time import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):  # might change these things, just copied from todo list i think
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):  # might change these things, just copied from todo list i think
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    role = db.Column(db.String(150))
    notes = db.relationship('Note')


class Nutrition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    calories = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    carbohydrates = db.Column(db.Integer)
    fats = db.Column(db.Integer)


class Sleep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    total_duration = db.Column(db.Integer)
    REM = db.Column(db.Integer)
    deep_sleep = db.Column(db.Integer)
    light_sleep = db.Column(db.Integer)


class Readiness(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    force = db.Column(db.Integer)
