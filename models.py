from app import db
from app import bcrypt

from app import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))

    def __init__(self, firstname, lastname, email, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password

class Ads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transactionType = db.Column(db.String(10))
    roomsNum = db.Column(db.Integer)
    area = db.Column(db.Integer)
    governorate = db.Column(db.String(200))
    location = db.Column(db.String(200))
    price = db.Column(db.Float)
    mobile = db.Column(db.Integer)
    description = db.Column(db.Text)

    def __init__(self, transactionType, roomsNum, area, governorate, location, price, mobile, description):
        self.transactionType = transactionType
        self.roomsNum = roomsNum
        self.area = area
        self.governorate = governorate
        self.price = price
        self.mobile = mobile        
        self.description = description

class Municipality(db.Model):
    id_mun = db.Column(db.Integer, primary_key=True)
    municipality = db.Column(db.String(60), primary_key=True)
  
class City(db.Model): 
    city = db.Column(db.String(60), primary_key=True)
    id_mun = db.Column(db.Integer) 
