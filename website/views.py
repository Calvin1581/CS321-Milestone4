from urllib import request
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Note

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
    return render_template("coachDashboard.html", user=current_user)


@views.route("/permissions")
def permissions():
    return render_template("permissions.html")

@views.route('/figures', methods=['GET', 'POST'])
@login_required
def figures():

    df = px.data.medals_wide()
    fig = px.bar(df, x="nation", y=["gold", "silver", "bronze"], title="Medals", barmode="group")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("figures.html", user=current_user, graphJSON=graphJSON)
