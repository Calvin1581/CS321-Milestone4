from tkinter.messagebox import NO
from urllib import request
from xml.dom.minidom import Identified
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
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
    try:
        list = User.query.all()
        
        user_list = list
        print(len(user_list))
    except:
        user_list = []
    id = request.form.get('users')
    if id:
        selected_user = User.query.filter_by(id=id).first()
    else:
        selected_user = current_user
    
    selected_role = "Athlete"

    if request.method == "POST":
        selected_role = request.form.get("select_role")
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name= request.form.get('last_name')
        password = request.form.get('password')
        role = request.form.get('roles')
        
        try:
            emailList = email.split('@')
        except:
            emailList = ["no","no"]
            
        
        try:
            user = User.query.filter_by(email=email).first()
        except:
            user = False
        if user:
            flash('Email already exists.', category='error')
        elif emailList[1] != 'colby.edu':
            flash('Must use colby email', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            
            # add user to database
            new_user = User(email=email,
                            password=generate_password_hash(password, method='sha256'),
                            role=role, first_name=first_name, last_name=last_name)

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)
            flash('Account created!', category='success')
    
        
    return render_template("permissions.html", user=current_user, user_list=user_list, selected_role=selected_role,selected_user=selected_user)
