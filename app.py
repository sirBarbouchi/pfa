from flask import (Flask, render_template, request, escape, flash,
                    url_for, redirect, make_response, session, Blueprint)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:13@localhost/pfa2'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\x1d\xcf\n\xe9\x0f*\xe2_Z\xdd\xdb\x19\xd8L\x1e\xaf\x058\x17\xbd\xa1_2\xf4'

db= SQLAlchemy(app)

from views.login import login

app.register_blueprint(login)





@app.route('/')

def index():
    return render_template("registration.html")
