from time import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from os.path import dirname
import pandas as pd
from datetime import datetime


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



def parse_csv(data_type: str, filename: str) -> None:
    """Parse a csv file."""
    # get the csv directory and merge it with filename
    csv_directory = f"{dirname(dirname(__file__))}/csvs"
    filepath = f"{csv_directory}/{filename}"
    # read the data from the csv
    csv_data = pd.read_csv(filepath_or_buffer=filepath, header=0)

    # conditional data ingestion
    if data_type == "user":
        data = []
        for row in csv_data.itertuples():
            # create a new User object
            user = User(
                email = row.email,
                first_name = row.first_name,
                last_name = row.last_name,
                password = row.password,
                role = row.role
            )
            # add the user to the database
            db.session.add(user)
            db.session.commit()

    elif data_type == "nutrition":
        data = []
        for row in csv_data.itertuples():
            # create a new Nutrition object
            nutrition = Nutrition(
                date = datetime.strptime(row.date, '%m/%d/%y'),
                calories = row.calories,
                protein = row.protein,
                carbohydrates = row.carbohydrates,
                fats = row.fats
            )
            # add the nutrition object to the database
            db.session.add(nutrition)
            db.session.commit()

    elif data_type == "readiness":
        data = []
        for row in csv_data.itertuples():
            # create a new Readiness object
            readiness = Readiness(
                date = datetime.strptime(row.date, '%m/%d/%y'),
                force = row.force
            )
            # add the readiness object to the database
            db.session.add(readiness)
            db.session.commit()

    # else, sleep data
    else:
        data = []
        for row in csv_data.itertuples():
            # create a new Sleep object
            sleep = Sleep(
                date = datetime.strptime(row.date, '%m/%d/%y'),
                total_duration = row.total_duration,
                REM = row.REM,
                deep_sleep = row.deep_sleep,
                light_sleep = row.light_sleep
            )
            # add the Sleep object to the database
            db.session.add(sleep)
            db.session.commit()
