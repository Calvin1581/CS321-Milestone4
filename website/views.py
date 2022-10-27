from urllib import request
from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for, current_app, redirect
from flask_login import login_required, current_user

from . import db
from .models import Note, parse_csv
from werkzeug.utils import secure_filename
import os

import pandas as pd

import json
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import sys

views = Blueprint('views', __name__)


@views.route("/")
def home():
    return redirect(url_for('auth.login'))


@views.route("/dashboard")
@login_required
def dashboard():
    dfR = pd.read_csv('website/data/readiness.csv')
    readinessAvg = dfR["Score"].mean().astype(int)

    dfS = pd.read_csv('website/data/sleep.csv')
    hoursAvg = dfS["Hours"].mean().astype(int)
    qualityAvg = dfS["Quality"].mean().astype(int)

    dfN = pd.read_csv('website/data/nutrition.csv')
    calAvg = dfN["Calorie Intake"].mean().astype(int)

    dfT = pd.read_csv('website/data/team.csv')
    teamValues1 = dfT["Hours"].tolist()
    teamValues2 = dfT["Readiness"].tolist()

    readinessL = ["Score"]
    readinessV = [readinessAvg]

    sleepL = ["Hours", "Quality"]
    h = [hoursAvg]
    q = [qualityAvg]

    nutritionL = ["Calorie Intake"]
    nutritionV = [calAvg]

    fig = make_subplots(rows=1, cols=4, column_widths=[.2, .2, .2, .5],
                        subplot_titles=["Readiness", "Sleep", "Nutrition",
                                        "Team Readiness"],
                        horizontal_spacing=0.1,
                        specs=[[{"type": "pie"}, {"type": "pie"},
                                {"type": "pie"}, {"type": "scatter"}]])

    # READINESS GRAPH
    fig.add_trace(go.Pie(values=readinessV, labels=readinessL, hole=.5,
                         title="Readiness", textfont=dict(color="white")),
                  row=1, col=1)

    # SLEEP GRAPH
    fig.add_trace(go.Pie(title="Sleep", hole=0.5, sort=False,
                         direction='clockwise', values=q,
                         textposition='inside',
                         marker={'line': {'color': 'white', 'width': 1}}),
                  row=1, col=2)

    fig.add_trace(go.Pie(hole=0.7, sort=False, direction='clockwise', values=h,
                         labels=sleepL, textposition='inside',
                         marker={'colors': ['green', 'red', 'blue'],
                                 'line': {'color': 'white', 'width': 1}}),
                  row=1, col=2)

    # NUTRITION GRAPH
    fig.add_trace(go.Pie(values=nutritionV, labels=nutritionL, hole=.5,
                         title="Nutrition", textfont=dict(color="white")),
                  row=1, col=3)

    # TEAM GRAPH
    fig.add_trace(go.Scatter(x=teamValues1, y=teamValues2), row=1, col=4)

    fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)',
                      'paper_bgcolor': 'rgba(0,0,0,0)', })

    fig.update_layout(margin=dict(l=50, r=0, t=0, b=0))
    fig.update_layout(showlegend=False)
    fig.update_layout(width=1100, height=300)
    fig.update_layout(font_color="white")
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("dashboard.html", user=current_user,
                           graphJSON=graphJSON)


@views.route("/athleteDashboard")
def athleteDashboard():

    dfR = pd.read_csv('website/data/readiness.csv')
    readinessAvg = dfR["Score"].mean().astype(int)

    dfS = pd.read_csv('website/data/sleep.csv')
    hoursAvg = dfS["Hours"].mean().astype(int)
    qualityAvg = dfS["Quality"].mean().astype(int)

    dfN = pd.read_csv('website/data/nutrition.csv')
    calAvg = dfN["Calorie Intake"].mean().astype(int)

    dfT = pd.read_csv('website/data/team.csv')
    teamValues1 = dfT["Hours"].tolist()
    teamValues2 = dfT["Readiness"].tolist()

    readinessL = ["Score"]
    readinessV = [readinessAvg]

    sleepL = ["Hours", "Quality"]
    h = [hoursAvg]
    q = [qualityAvg]

    nutritionL = ["Calorie Intake"]
    nutritionV = [calAvg]
    
    fig = make_subplots(rows=1, cols=4, column_widths=[.2,.2,.2,.5], subplot_titles=["Readiness", "Sleep", "Nutrition", "John Doe's Trends"], horizontal_spacing = 0.1, specs=[ [{"type": "pie"}, {"type": "pie"}, {"type": "pie"}, {"type": "scatter"} ]] )

    # READINESS GRAPH
    fig.add_trace(go.Pie(values=readinessV, labels=readinessL, hole=.5, title="Readiness", textfont=dict(color="white")), row=1, col=1)
    
    # SLEEP GRAPH
    fig.add_trace(go.Pie(title="Sleep", hole=0.5, sort=False, direction='clockwise', values=q, textposition='inside', marker={'line': {'color': 'white', 'width': 1}}), row=1, col=2)
    fig.add_trace(go.Pie(hole=0.7, sort=False, direction='clockwise', values=h, labels=sleepL, textposition='inside', marker={'colors': ['green', 'red', 'blue'], 'line': {'color': 'white', 'width': 1}}), row=1, col=2)

    # NUTRITION GRAPH
    fig.add_trace(go.Pie(values=nutritionV, labels=nutritionL, hole=.5, title="Nutrition", textfont=dict(color="white")), row=1, col=3)

    # TEAM GRAPH
    fig.add_trace(go.Scatter(x=teamValues1, y=teamValues2), row=1, col=4)

    fig.update_layout({ 'plot_bgcolor': 'rgba(0,0,0,0)',  'paper_bgcolor': 'rgba(0,0,0,0)', })
    fig.update_layout(margin=dict(l=50, r=0, t=0, b=0))
    fig.update_layout(showlegend=False)
    fig.update_layout(width=1100, height=300)
    fig.update_layout(font_color="white")
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template("athleteDashboard.html", user=current_user, graphJSON=graphJSON)


@views.route("/coachDashboard")
def coachDashboard():

    dfR = pd.read_csv('website/data/readiness.csv')
    readinessAvg = dfR["Score"].mean().astype(int)

    dfS = pd.read_csv('website/data/sleep.csv')
    hoursAvg = dfS["Hours"].mean().astype(int)
    qualityAvg = dfS["Quality"].mean().astype(int)

    dfN = pd.read_csv('website/data/nutrition.csv')
    calAvg = dfN["Calorie Intake"].mean().astype(int)

    dfT = pd.read_csv('website/data/team.csv')
    teamValues1 = dfT["Hours"].tolist()
    teamValues2 = dfT["Readiness"].tolist()

    readinessL = ["Score"]
    readinessV = [readinessAvg]

    sleepL = ["Hours", "Quality"]
    h = [hoursAvg]
    q = [qualityAvg]

    nutritionL = ["Calorie Intake"]
    nutritionV = [calAvg]

    fig = make_subplots(rows=1, cols=4, column_widths=[.2, .2, .2, .5],
                        subplot_titles=["Readiness", "Sleep", "Nutrition",
                                        "Team Readiness"],
                        horizontal_spacing=0.1,
                        specs=[[{"type": "pie"}, {"type": "pie"},
                                {"type": "pie"}, {"type": "scatter"}]])

    # READINESS GRAPH
    fig.add_trace(go.Pie(values=readinessV, labels=readinessL, hole=.5,
                         title="Readiness", textfont=dict(color="white")),
                  row=1, col=1)

    # SLEEP GRAPH
    fig.add_trace(go.Pie(title="Sleep", hole=0.5, sort=False,
                         direction='clockwise', values=q,
                         textposition='inside',
                         marker={'line': {'color': 'white', 'width': 1}}),
                  row=1, col=2)

    fig.add_trace(go.Pie(hole=0.7, sort=False, direction='clockwise', values=h,
                         labels=sleepL, textposition='inside',
                         marker={'colors': ['green', 'red', 'blue'],
                                 'line': {'color': 'white', 'width': 1}}),
                  row=1, col=2)

    # NUTRITION GRAPH
    fig.add_trace(go.Pie(values=nutritionV, labels=nutritionL, hole=.5,
                         title="Nutrition", textfont=dict(color="white")),
                  row=1, col=3)

    # TEAM GRAPH
    fig.add_trace(go.Scatter(x=teamValues1, y=teamValues2), row=1, col=4)

    fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)',
                      'paper_bgcolor': 'rgba(0,0,0,0)', })

    fig.update_layout(margin=dict(l=50, r=0, t=0, b=0))
    fig.update_layout(showlegend=False)
    fig.update_layout(width=1100, height=300)
    fig.update_layout(font_color="white")
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template("coachDashboard.html", user=current_user,
                           graphJSON=graphJSON)


@views.route("/permissions")
def permissions():
    return render_template("permissions.html")

@views.route("/athleteSleepData")
def athleteSleep():
    return render_template("athleteSleepData.html")

@views.route("/athleteReadiness")
def athleteReadiness():
    return render_template("athleteReadinessData.html")

@views.route("/athleteNutrition")
def athleteNutrition():
    return render_template("athleteNutritionData.html")

# helper function for upload()
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {"csv"}

@views.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            # parse the csv file and insert it into the db
            data_type = filename.rsplit(".")[0].lower()
            parse_csv(data_type=data_type, filename=filename)
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


