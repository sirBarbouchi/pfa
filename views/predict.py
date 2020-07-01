from flask import Flask, render_template, request, jsonify, json, Blueprint, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy  
from wtforms import SelectField, Form
from flask_wtf import FlaskForm
from flask_login import current_user
from views.forms import Form
from models import Region, Municipality, Emplacement
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
import joblib


model=pickle.load(open('model.pkl','rb'))


sc_X = joblib.load("data_transformer.joblib") 
 
pred = Blueprint('pred', __name__, template_folder='templates')
def transf(l):
    a = [12, 19, 20, 29, 34, 44, 48,  0,  1, 13, 15, 30, 31, 33, 46, 50,  8,
        4,  6, 16, 21, 22, 23, 55,  2, 24,  5, 45, 52,  9, 35, 38, 47,  7,
       54, 36, 37, 39, 40, 42, 51, 26, 27, 28, 43, 56, 18, 25, 32, 17, 49,
        3, 14, 10, 11, 41, 53]
    l0 = [0]*59
    l0[-1], l0[-2] = l[-1], l[-2]
    l0[a[l[0]-1]-1] = 1
    return l0

         
@pred.route('/predict', methods=['GET', 'POST'])
def predict():
    print("*******",session['logged_in'])
    session['predict']=True
    if not session['logged_in'] :
        return redirect(url_for('auth.login'))
        #return redirect(url_for('auth.login'))
    form = Form()
    form.municipality.choices = [(municipality.id_mun, municipality.municipality) for municipality in Municipality.query.all()]
    form.municipality.default = '1'
    if request.method == 'POST':
        municipality = Municipality.query.filter_by(id=form.municipality.data).first()
        city = city.query.filter_by(id=form.city.data).first()
        area = int(form.area.data)
        roomNumber = int(form.roomNumber.data)
        emp = 1#emplacement.id
        int_features = [emp, roomNumber, area]
        final = np.array(transf(int_features)).reshape(-1, 59)
        print("**" , final)

        final[:,57:] = sc_X.transform(final[:,57:]) 
        print("**" , final)

        prediction = model.predict(final)

        return render_template('price.html',price=round(prediction[0], 2))
    return render_template('predict.html', form=form)
 
@pred.route('/city/<get_city>')###
def citybyregion(get_city):
    city = City.query.filter_by(id_mun=get_city).all()
    cityArray = []
    for c in city:
        cityObj = {}
        cityObj['name'] = c.municipality
        cityArray.append(cityObj)
    return jsonify({'citymunicipality' : cityArray})
