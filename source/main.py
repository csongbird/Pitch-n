from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .app import app as flask_app
import os

main = Blueprint('main', __name__)
IMAGES_FOLDER = os.path.join('static', 'images')
flask_app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER


@main.route('/profile')
@login_required
def profile():
    print("LOGGING IN USER")
    pic = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'profilePic.png')
    center1 = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'center1.png')
    center2 = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'center2.png')
    center3 = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'center3.png')
    center4 = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'center4.png')
    return render_template('profile.html', name=current_user.username,
                           profilePic=pic, center1=center1, center2=center2,
                           center3=center3, center4=center4)


@main.route('/organization')
@login_required
def organization():
    print("LOGGING IN ORG")
    return render_template('organization.html', name=current_user.username)
