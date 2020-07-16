from flask import Flask
from flask import render_template,redirect,request
import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_log_error
from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import accuracy_score
from test import prediction

app=Flask(__name__)
    

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/result", methods = ['POST', 'GET'])
def result():
    if request.method=='POST':
        age=request.form["age"]
        serum_cholestoral=request.form["serum_cholestoral"]
        chest=request.form["chest"]	
        resting_blood_pressure=request.form["resting_blood_pressure"]
        maximum_heart_rate_achieved=request.form["maximum_heart_rate_achieved"]
        oldpeak=request.form["oldpeak"]
        thal=request.form["thal"]
        sex=request.form["age"]
        fasting_blood_sugar=request.form['fasting_blood_sugar']	
        resting_electrocardiographic_results=request.form['resting_electrocardiographic_results']		
        exercise_induced_angina=request.form['exercise_induced_angina']
        slope=request.form['slope']
        number_of_major_vessels=request.form['number_of_major_vessels']
        lst=list()
        lst.append((age))
        lst.append((sex))
        lst.append((chest))
        lst.append((resting_blood_pressure))
        lst.append((serum_cholestoral))
        lst.append((fasting_blood_sugar))
        lst.append((resting_electrocardiographic_results))
        lst.append((maximum_heart_rate_achieved))
        lst.append((exercise_induced_angina))
        lst.append((oldpeak))
        lst.append((slope))
        lst.append((number_of_major_vessels))
        lst.append((thal))
        result=prediction(lst)
        return render_template("result.html",result=result,lst=lst)



    else:
        return render_template("index.html")

if __name__=='__main__':
    app.run( debug=True)