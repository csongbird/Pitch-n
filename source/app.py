from flask import Flask, Blueprint, render_template
from flask import redirect, url_for, request, flash
from .models import User, Organization
from flask_login import logout_user
from .maps import generate_map
from .__init__ import database, create_app
from .db import get_user, add_user, get_org, add_org
import os

auth = Blueprint('auth', __name__)

app = Flask(__name__)
IMAGES_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database.create_all(app=create_app())


@auth.route('/')
@app.route('/')
@auth.route('/login')
@app.route('/login')
@auth.route('/index.html')
@app.route('/index.html')
def login():
    """
    Shows the Homepage
    """
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    background = os.path.join(app.config['UPLOAD_FOLDER'], 'background.png')
    return render_template('index.html', logo=logo, background=background)


@app.route('/signup')
@auth.route('/signup')
def signup():
    """
    Shows the registration page
    """
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template('register.html', logo=logo)


@app.route('/signup', methods=['POST'])
@auth.route('/signup', methods=['POST'])
def signup_post():
    """
    Gets information from the registration page, and puts it
    in the data base
    """
    email = request.form.get('email')
    username = request.form.get('uname')
    password = request.form.get('psw')
    center = True if request.form.get('yes') else False

    if center:
        name = request.form.get('name')
        location = request.form.get('loc')

        org = get_org(email, username, password, name, location)
        if org[1] == 200:
            flash('Email address already exists')
            try:
                return redirect(url_for('auth.signup'))
            except Exception:
                return redirect(url_for('signup'))
        add_org(email, username, password, name, location)
    else:
        # if this returns a user, then the email already exists in database
        user = get_user(email, username, password)
        if user[1] == 200:
            flash('Email address already exists')
            try:
                return redirect(url_for('auth.signup'))
            except Exception:
                return redirect(url_for('signup'))

        add_user(email, username, password)

    try:
        return redirect(url_for('auth.login'))
    except Exception:
        return redirect(url_for('login'))


@app.route('/login', methods=['POST'])
@auth.route('/login', methods=['POST'])
def login_post():
    """
    Used to log in a Donator or a Donation Center
    """
    print('Trying to log in...')
    name = request.form.get('uname')
    password = request.form.get('psw')
    remember = True if request.form.get('remember') else False

    log_in = get_user(name, name, password)
    user = True
    if log_in[1] != 200:
        print("Getting User")
        log_in = get_org(name, name, password, "", "")
        user = False
    if log_in[1] != 200:
        flash('Please check your login details and try again.')
        # if the user doesn't exist or password is wrong, reload the page
        try:
            return redirect(url_for('auth.login'))
        except Exception:
            return redirect(url_for('login'))
    print(log_in)
    if user:
        print("Logging in User")
        User.login(log_in[0]['email'],
                   log_in[0]['username'],
                   password,
                   remember)
        return redirect(url_for('main.profile'))
    print("Logging in Organization")
    Organization.login(log_in[0]['email'],
                       log_in[0]['username'],
                       password,
                       remember)
    print("Done logging in")
    print(log_in)
    try:
        return redirect(url_for('main.organization',
                        org_id=log_in[0]['org_id']))
    except Exception as e:
        print(e)


@auth.route("/explore.html")
@app.route("/explore.html")
def show_explore():
    """
    Shows Map
    """
    generate_map()
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template('explore.html', logo=logo)


@app.route('/logout')
@auth.route('/logout')
def logout():
    """
    Log outs a signed in user
    """
    logout_user()
    try:
        return redirect(url_for('auth.login'))
    except Exception:
        return redirect(url_for('login'))
