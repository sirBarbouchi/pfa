from app import db


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
