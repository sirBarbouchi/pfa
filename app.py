from flask import Flask
from flask import render_template , url_for
from flask_sqlalchemy import SQLAlchemy
from flask import request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresql:123@localhost/Pfa2'
db= SQLAlchemy(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


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
    return render_template("index.html")
@app.route('/new', methods=['POST', 'GET'])
def createAccount():
    firstName = request.form.get('FirstName')
    lastName = request.form.get('LastName')
    email = request.form.get('Email')
    password = request.form.get('Password')
    username = request.form.get('Username')
    user = Users(firstName, lastName, email, username, password)
    db.session.add(user)
    db.session.commit()
    return render_template('index.html')
if __name__== "__main__":
    app.run(debug=True, )
