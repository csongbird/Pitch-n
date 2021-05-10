from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from .app import app as flask_app
from .models import Organization
import os

main = Blueprint('main', __name__)
IMAGES_FOLDER = os.path.join('static', 'images')
flask_app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER
furniture = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'furniture.png')
clothing = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'clothes.png')
housewares = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'pan.png')
electronics = os.path.join(flask_app.config['UPLOAD_FOLDER'],
                           'electronics.png')
food = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'food.png')
logo = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'logo.png')
books = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'books.png')
instructions = os.path.join(flask_app.config['UPLOAD_FOLDER'],
                            'instructions.png')


@main.route('/profile')
@login_required
def profile():
    pic = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'userImg.png')
    center1 = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'center1.png')
    center2 = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'center2.png')
    center3 = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'center3.png')
    center4 = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'center4.png')
    return render_template('profile.html', logo=logo,
                           name=current_user.username,
                           profilePic=pic, center1=center1,
                           center2=center2,
                           center3=center3, center4=center4)


@main.route('/organization')
@login_required
def organization():
    pic = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'userImg.png')
    org_id = request.args.get('org_id')
    current_user = Organization.get_org_with_id(org_id)
    return render_template('organization.html',
                           name=current_user.username,
                           centerName=current_user.name,
                           location=current_user.location,
                           clothing=clothing,
                           furniture=furniture,
                           housewares=housewares,
                           food=food, books=books,
                           electronics=electronics,
                           logo=logo,
                           pic=pic)


# Code below is hard-coded demo code used for presentation
@main.route('/center1.html')
def center1():
    pic = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'center1.png')
    return render_template('center1.html', logo=logo,
                           pic=pic,
                           name="Callahan's Castaways",
                           clothing=clothing,
                           furniture=furniture, instructions=instructions,
                           housewares=housewares)


@main.route('/center2.html')
def center2():
    pic = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'center2.png')
    return render_template('center2.html', logo=logo,
                           pic=pic,
                           name="Tanya's Terrific Givers",
                           clothing=clothing, instructions=instructions,
                           furniture=furniture,
                           housewares=housewares,
                           food=food, books=books,
                           electronics=electronics)


@main.route('/center3.html')
def center3():
    pic = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'center3.png')
    return render_template('center3.html', logo=logo,
                           pic=pic, instructions=instructions,
                           name="Avik's Able Homes",
                           clothing=clothing,
                           furniture=furniture, books=books,
                           housewares=housewares)


# Code below is hard-coded demo code used for presentation
@main.route('/center4.html')
def center4():
    pic = os.path.join(flask_app.config['UPLOAD_FOLDER'], 'center4.png')
    return render_template('center4.html', logo=logo,
                           pic=pic, instructions=instructions,
                           name="Crystal Clear Cause",
                           clothing=clothing,
                           furniture=furniture, food=food,
                           electronics=electronics)
