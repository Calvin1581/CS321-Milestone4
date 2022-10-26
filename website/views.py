from urllib import request
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Note

import os
import sys
from flask import Flask, flash, request, redirect, url_for, current_app
from werkzeug.utils import secure_filename

views = Blueprint('views', __name__)


@views.route("/")
def home():
    return "<h1>Howdy milestone 4ers</h1>"


@views.route("/athleteDashboard")
def athleteDashboard():
    return render_template("athleteDashboard.html", user=current_user)


@views.route("/coachDashboard")
def coachDashboard():
    return render_template("coachDashboard.html", user=current_user)


@views.route("/permissions")
def permissions():
    return render_template("permissions.html")


# helper function for upload()
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {"csv"}

@views.route("/upload", methods=["GET", "POST"])
def upload():
    sys.stdout.flush()
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        sys.stdout.flush()
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for("views.upload"))

    # basic, flask-provided html for uploading files
    # TODO make an actual webpage that imlements this
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


