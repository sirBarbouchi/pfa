from flask import render_template, Blueprint
from models import Users
from models import db


login = Blueprint('login', __name__)

@login.route('/new', methods=['POST', 'GET'])
def createAccount():
    if request.method == "POST":
        firstName = request.form.get('FirstName')
        lastName = request.form.get('LastName')
        email = request.form.get('Email')
        password = request.form.get('Password')
        username = request.form.get('Username')
        user = Users(firstName, lastName, email, username, password)
        db.session.add(user)
        db.session.commit()
    return render_template("index.html")