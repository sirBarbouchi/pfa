from flask import render_template, Blueprint, request, url_for, flash, redirect, request, session
from models import Users
from models import db, bcrypt
from views.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        #user = Users(firstName, lastName, email, username, password)
        user = Users(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        #session['logged_in'] = True

        return redirect(url_for('auth.login'))
    return render_template('registration.html', title='Register', form=form)


@auth.route("/login", methods=['GET', 'POST'])

def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            session['logged_in'] = True
            if "predict" in session:
                if session['predict']==True:
                    return redirect('/predict')
             
            return redirect(url_for('app.home'))
            #flash('Login successful.', 'success')
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
            return redirect(url_for('auth.redirected'))
    return render_template('login.html', title='Login', form=form)

@auth.route("/redirected", methods=['GET', 'POST'])
def redirected():
    return redirect(url_for('auth.login'))


@auth.route("/logout")
def logout():
    logout_user()
    session['logged_in'] = False
    return redirect(url_for('home'))

