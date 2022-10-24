from urllib import request
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Note

views = Blueprint('views', __name__)


@views.route("/")
def home():
    return render_template("login.html")


@views.route("/athleteDashboard")
def athleteDashboard():
    return render_template("athleteDashboard.html", user=current_user)


@views.route("/coachDashboard")
def coachDashboard():
    return render_template("coachDashboard.html", user=current_user)


@views.route("/permissions")
def permissions():
    return render_template("permissions.html")

@views.route("/signup")
def signUp():
    return render_template("signup.html")
