import flask
from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('tempcreate.html')
app.run()
