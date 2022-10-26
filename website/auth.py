from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.dashboard'))
            else:
                flash('Incorrect password')
        else:
            flash('Email does not exist')

    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        role = request.form.get('role')
        print(role)

        emailList = email.split('@')

        user = User.query.filter_by(email=email).first()
        if email == '':
            flash('Email required')
        elif user:
            flash('Email already exists.')
        elif len(emailList) < 2:
            flash('Invalid email')
        elif emailList[1] != 'colby.edu':
            flash('Must use colby email')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.')
        elif len(first_name)==0:
            flash('First name required')
        elif len(last_name)==0:
            flash('Last name required')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.')
        elif password != confirm_password:
            flash('Passwords don\'t match.')
        else:
            # add user to database
            new_user = User(email=email,
                            password=generate_password_hash(password, method='sha256'),
                            role=role, first_name=first_name, last_name=last_name)

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('views.dashboard'))

    return render_template("signup.html", user=current_user)
