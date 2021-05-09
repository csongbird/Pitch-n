from flask import Flask, Blueprint, render_template
from flask import redirect, url_for, request, flash
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Organization
from .maps import generate_map
from .__init__ import database, create_app
import os

auth = Blueprint('auth', __name__)

app = Flask(__name__)
IMAGES_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER
database.create_all(app=create_app())


@auth.route('/')
@app.route('/')
@auth.route('/login')
@app.route('/login')
@auth.route('/index.html')
@app.route('/index.html')
def login():
    print("INDEX")
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
    username = request.form.get('uname')
    password = request.form.get('psw')
    # if this returns a user, then the email already exists in database
    user = User.query.filter(
        User.email == email or User.username == username
    ).first()
    # if a user is found, we want to redirect back to signup page
    if user:
        flash('Email address already exists')
        try:
            return redirect(url_for('auth.signup'))
        except Exception:
            return redirect(url_for('signup'))

    # this means registration is for a center
    center = True if request.form.get('yes') else False

    # create a new user with the form data.
    # Hash the password so the plaintext version isn't saved.
    if (not center and email and username and password):
        new_user = User(
            email=email,
            username=username,
            password=generate_password_hash(password, method='sha256')
        )

    # create a new center with the form data
    if (center):
        print("GOT A CENTER")
        name = request.form.get('name')
        location = request.form.get('loc')
        new_user = Organization(name, username, password, location, email)

    # add the new user to the database
    database.session.add(new_user)
    database.session.commit()
    try:
        return redirect(url_for('auth.login'))
    except Exception:
        return redirect(url_for('login'))


@app.route('/login', methods=['POST'])
@auth.route('/login', methods=['POST'])
def login_post():
    print("TRYING TO LOG IN")
    name = request.form.get('uname')
    password = request.form.get('psw')
    remember = True if request.form.get('remember') else False

    user = User.query.filter(
        User.username == name or User.email == name
    ).first()

    center = Organization.query.filter(
        Organization.email == name or Organization.username == name
    ).first()

    if center:
        print('TRYING TO LOG IN CENTER')
        print(center)
        login_user(center, remember=remember)
        return redirect(url_for('main.organization'))
    # check if the user actually exists
    # take the user-supplied password, hash it,
    # and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        print("DONT HAVE A USER")
        flash('Please check your login details and try again.')
        # if the user doesn't exist or password is wrong, reload the page
        try:
            return redirect(url_for('auth.login'))
        except Exception:
            return redirect(url_for('login'))

    # if the above check passes,then we know the user has the right credentials
    print('TRYING TO LOG IN USER')
    print(user.json())
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route("/explore.html")
@app.route("/explore.html")
def show_explore():
    generate_map()
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template('explore.html', logo=logo)


@app.route('/logout')
@auth.route('/logout')
def logout():
    return 'Logout'
