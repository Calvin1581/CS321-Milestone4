from urllib import request
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
#from . import db
#from .models import Note
import pandas as pd

import json
import plotly
import plotly.express as px

views = Blueprint('views', __name__)


@views.route("/")
def home():
    return "<h1>Howdy milestone 4ers</h1>"


@views.route("/athleteDashboard")
def athleteDashboard():
    return render_template("athleteDashboard.html", user=current_user)


@views.route("/coachDashboard")
def coachDashboard():
    
    df = pd.read_csv('website/data/sleep.csv')
    hoursAvg = df["Hours"].mean().astype(int)

    labels = ["Hours"]
    values = [hoursAvg]
    
    fig = px.pie(labels, values = values, hole = 0.4, width=280, height=280, color = labels, color_discrete_map = {'Hours':'blue'})

    fig.update_layout({
        'plot_bgcolor': 'rgba(0,0,0,0)', 
        'paper_bgcolor': 'rgba(0,0,0,0)',
        })

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("coachDashboard.html", user=current_user, graphJSON=graphJSON)

@views.route("/permissions")
def permissions():
    return render_template("permissions.html")
