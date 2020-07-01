<<<<<<< HEAD
from flask import (Flask, render_template, request, escape, flash, json, jsonify,
                    url_for, redirect, make_response, session, Blueprint)
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from datetime import timedelta
from flask_login import current_user

from flask_sqlalchemy import SQLAlchemy

from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:09869839@localhost/Pfa2'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\x1d\xcf\n\xe9\x0f*\xe2_Z\xdd\xdb\x19\xd8L\x1e\xaf\x058\x17\xbd\xa1_2\xf4'
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
# oAuth Setup
oauth = OAuth(app)


db= SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from views.login import auth
app.register_blueprint(auth)

from views.google import auth2
app.register_blueprint(auth2)


from views.predict import pred
app.register_blueprint(pred)


@app.route('/')
def home():
    session['predict']=False
    return render_template("index.html")
    #return render_template("index.html")


@app.route('/about')
def about():
    session['predict']=False
=======
from flask import (Flask, render_template, request, escape, flash, json, jsonify,
                    url_for, redirect, make_response, session, Blueprint)
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from datetime import timedelta
from flask_login import current_user

from flask_sqlalchemy import SQLAlchemy

from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:09869839@localhost/Pfa2'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\x1d\xcf\n\xe9\x0f*\xe2_Z\xdd\xdb\x19\xd8L\x1e\xaf\x058\x17\xbd\xa1_2\xf4'
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
# oAuth Setup
oauth = OAuth(app)


db= SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from views.login import auth
app.register_blueprint(auth)

from views.google import auth2
app.register_blueprint(auth2)


from views.predict import pred
app.register_blueprint(pred)


@app.route('/')
def home():
    session['predict']=False
    return render_template("index.html")
    #return render_template("index.html")


@app.route('/about')
def about():
    session['predict']=False
>>>>>>> 519083e4bba3ed62676dda3777e51431bc46f999
    return render_template("about.html")