from flask import Flask, render_template
import os

IMAGES_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER


@app.route("/")
@app.route("/index.html")
def show_index():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    background = os.path.join(app.config['UPLOAD_FOLDER'], 'background.png')
    return render_template('index.html', logo=logo, background=background)


@app.route("/donate.html")
def show_donate():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    background = os.path.join(app.config['UPLOAD_FOLDER'], 'background.png')
    return render_template('donate.html', logo=logo, background=background)


@app.route("/explore.html")
def show_explore():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    background = os.path.join(app.config['UPLOAD_FOLDER'], 'background.png')
    return render_template('explore.html', logo=logo, background=background)


app.run(debug=True)
