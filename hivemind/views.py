from flask import render_template
from hivemind import app

@app.route('/')
def hello_world():
    return render_template('index.html')

