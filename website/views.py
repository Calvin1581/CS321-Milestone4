from urllib import request
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Note


views = Blueprint('views', __name__)


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/coach-dashboard")
def coach_dashboard():
    return render_template("coachDashboard.html")


@views.route("/coach-athlete-view")
def coach_athlete_view():
    return render_template("coachAthleteView.html")


@views.route("/athlete-nutrition")
def athlete_nutrition_data():
    return render_template("athleteNutritionData.html")


@views.route("/athlete-readiness")
def athlete_readiness_data():
    return render_template("athleteReadinessData.html")


@views.route("/athlete-sleep")
def athlete_sleep_data():
    return render_template("athleteSleepData.html")


@views.route("/athlete-dashboard")
def athlete_dashboard():
    return render_template("athleteDashboard.html")


@views.route("/admin-dashboard")
def admin_dashboard():
    return render_template("adminPeakDashboard.html")


@views.route("/admin-team-view")
def admin_team_view():
    return render_template("adminPeakTeamView.html")


@views.route("/admin-athlete-view")
def admin_athlete_view():
    return render_template("adminPeakAthleteView.html")


@views.route("/admin-permissions")
def admin_permissions():
    return render_template("permissions.html")


