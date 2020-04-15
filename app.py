from flask import Flask
from flask import render_template , url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresql:09869839@localhost/Pfa2'
db= SQLAlchemy(app)

class Users(db.Model):
    FirstName = db.Column(db.String(200))
    LastName = db.Column(db.String(200))
    Email = db.Column(db.String(200), unique=True)
    Username = db.Column(db.String(200), primary_key=True)    
    Password = db.Column(db.String(200))

    def __init__(self, FirstName, LastName, Email, Username, Password):
        self.FirstName=FirstName
        self.LastName=LastName
        self.Email=Email
        self.Username=Username
        self.Password=Password

    #def __repr__(self)



@app.route('/')

def index():
    return render_template("index.html")

if __name__== "__main__":
    app.run(debug=True)