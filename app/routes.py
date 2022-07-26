from flask import render_template
from app import app

@app.route("/")
@app.route('/index')
def index():
    user = {"username": "Natalie"}
    kind_dict = ['soup', 'side', 'main']
    return render_template("index.html", title="Home", user=user, kind_dict=kind_dict[0])

