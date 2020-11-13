import os
from flask import Flask, render_template, flash, request, url_for, redirect
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/uploadFiles'
ALLOWED_EXTENSIONS = {'txt','pdf'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/') #good
def mainPage():
    return render_template('mainpage.html')

@app.route('/Perihal') #good
def perihal():
    return render_template('perihal.html')

@app.route('/Upload', methods = ['GET','POST']) #masih bad
def uploadPage():
    return ("ini page buat upload")

if __name__ == '__main__':
    app.run()
