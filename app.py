from flask import (Flask, render_template, request, escape, flash,
                    url_for, redirect, make_response, session, Blueprint)
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/pfa2'
db= SQLAlchemy(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\x1d\xcf\n\xe9\x0f*\xe2_Z\xdd\xdb\x19\xd8L\x1e\xaf\x058\x17\xbd\xa1_2\xf4'


class Users(db.Model):
    firstName = db.Column(db.String(200))
    lastName = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    username = db.Column(db.String(200), primary_key=True)
    password = db.Column(db.String(200))

    def __init__(self, firstName, lastName, email, username, password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.password = password

    #def __repr__(self)



@app.route('/')

def index():
    return render_template("registration.html")
@app.route('/new', methods=['POST', 'GET'])
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
if __name__== "__main__":
    app.run(debug=True)