# AS simeple as possbile flask google oAuth 2.0
from flask import render_template, Blueprint, request, url_for, flash, redirect, request, session
from models import Users
from models import db, bcrypt

from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os
from app import oauth
# decorator for routes that should be accessible only by logged in users
# oAuth Setup
'''
# dotenv setup
from dotenv import load_dotenv
load_dotenv()'''

auth2 = Blueprint('auth2', __name__, template_folder='templates')
# App config
# Session config
#auth2.secret_key = os.getenv("APP_SECRET_KEY")
google = oauth.register(
    name='google',
    client_id="554055143252-3l2334op10f142l9psn3ojg1qk20gkbk.apps.googleusercontent.com",
    client_secret="q7iBBtPh-7cVoDKuAjiOLN00",
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)

@auth2.route('/login2')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    #next_page = request.args['messages']
    redirect_uri = url_for('auth2.authorize', _external=True )
    return google.authorize_redirect(redirect_uri)


@auth2.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    user1 = dict(session).get('profile', None)
    #login_user(user1)

    #print("/*/*/*/*/*/*/**",user1.get("email"))
    session['logged_in'] = True
    logged = True
    print("lllllllll",logged)
    session['profile'] = user_info
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    if session['predict']==True:
        return redirect('/predict')
    return redirect('/')

"""
@auth2.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')
"""