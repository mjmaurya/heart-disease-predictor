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
@app.route("/result")
def result():
    lst=[70,1,4,130,322,0,2,109,0,2.4,2,3,3]
    result=prediction(lst)
    return render_template("result.html",result=result)
if __name__=='__main__':
    app.run( debug=True)