import os
from flask import Flask, render_template, flash, request
app = Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('mainpage.html')

@app.route('/Upload')
def uploadPage():
    return ("ini page buat upload")

if __name__ == '__main__':
    app.run()
