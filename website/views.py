from urllib import request
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Note

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return "<h1>Howdy milestone 4ers</h1>"