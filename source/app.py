from flask import Flask, request, render_template, redirect, url_for
import os
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

IMAGES_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER


@app.route("/")
@app.route("/index.html", methods=["POST", "GET"])
def show_index():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    background = os.path.join(app.config['UPLOAD_FOLDER'], 'background.png')
    if request.method == "POST":
        user = request.form["uname"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template('index.html', logo=logo, background=background)


@app.route("/explore.html")
def show_explore():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template('explore.html', logo=logo)


@app.route("/<usr>")
def user(usr):
    return f"<h1>Welcome {usr}</h1>"

# @app.route("/login")
# def login():
#   return render_template


app.run(debug=True)
