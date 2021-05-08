from flask import Flask, Blueprint, render_template
from flask import redirect, url_for, request, flash
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
import os

auth = Blueprint('auth', __name__)

app = Flask(__name__)
IMAGES_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER


@auth.route('/')
@app.route('/')
@auth.route('/login')
@app.route('/login')
@auth.route('/index.html')
@app.route('/index.html')
def login():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    background = os.path.join(app.config['UPLOAD_FOLDER'], 'background.png')
    return render_template('index.html', logo=logo, background=background)


@app.route('/signup')
@auth.route('/signup')
def signup():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template('register.html', logo=logo)


@app.route('/signup', methods=['POST'])
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('uname')
    password = request.form.get('psw')
    # if this returns a user, then the email already exists in database
    user = User.query.filter(
        User.email == email or User.username == name
    ).first()
    # if a user is found, we want to redirect back to signup page
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data.
    # Hash the password so the plaintext version isn't saved.
    if (email and name and password):
        new_user = User(
            email=email,
            username=name,
            password=generate_password_hash(password, method='sha256')
        )

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@app.route('/login', methods=['POST'])
@auth.route('/login', methods=['POST'])
def login_post():
    name = request.form.get('uname')
    password = request.form.get('psw')
    remember = True if request.form.get('remember') else False

    user = User.query.filter(
        User.username == name or User.email == name
    ).first()

    # check if the user actually exists
    # take the user-supplied password, hash it,
    # and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        # if the user doesn't exist or password is wrong, reload the page
        return redirect(url_for('auth.login'))

    # if the above check passes,then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@app.route("/explore.html")
def show_explore():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template('explore.html', logo=logo)


@app.route('/logout')
@auth.route('/logout')
def logout():
    return 'Logout'
