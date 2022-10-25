from urllib import request
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from os.path import join, dirname, realpath
from . import db
from .models import Note
from .csvParse import parseCSV


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

@views.route("/upload", methods = ['GET','POST'])
def uploadFiles():
    #get uploaded file
    if request.method == 'POST':

        uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'],uploaded_file.filename)
        #set the file path
        uploaded_file.save(file_path)
        parseCSV(file_path)
    return render_template('upload.html')
