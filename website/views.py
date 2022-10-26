from urllib import request
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import User,Note

views = Blueprint('views', __name__)


@views.route("/")
def home():
    return "<h1>Howdy milestone 4ers</h1>"


@views.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", user=current_user)


@views.route("/athleteDashboard")
def athleteDashboard():
    return render_template("athleteDashboard.html", user=current_user)


@views.route("/coachDashboard")
def coachDashboard():
    return render_template("coachDashboard.html", user=current_user)


@views.route("/permissions", methods=['GET', 'POST'])
def permissions():
    selected_user = User.query.filter_by(id=request.form.get('users')).first()
    selected_role = request.form.get('select_role')

    list = User.query.all()
    if list.first():

        user_list = list
    else:
        
        user_list = [];
    return render_template("permissions.html", user=current_user, user_list=user_list,chosen_user=selected_user,selected_role=selected_role)
