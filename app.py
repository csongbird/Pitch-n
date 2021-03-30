from flask import Flask, request, render_template
import os

IMAGES_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER

@app.route("/")
@app.route("/index")
def show_index():
	logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
	background = os.path.join(app.config['UPLOAD_FOLDER'], 'background.png')
	return render_template('index.html', logo=logo, background=background)

app.run(debug = True)
