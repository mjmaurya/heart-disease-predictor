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




def prediction(new_data):
    new_data=np.array(new_data)
    new_data=new_data.reshape(1,13)
    result=logr.predict(new_data)
    return result[0]
df=pd.read_csv('heart-data.csv')
df.rename(columns={"class":"target"},inplace=True)
df['target'].replace(['absent','present'],[0,1],inplace=True)
df=pd.get_dummies(df)
x=df.drop('target', axis=1)
y=df['target']
train_x,valid_x,train_y,valid_y=train_test_split(x,y,test_size=0.3,random_state=35)
logr=LogisticRegression()
logr.fit(train_x,train_y)
pred_test=logr.predict(valid_x)
new_data=[70,1,4,130,322,0,2,109,0,2.4,2,3,3]
print(prediction(new_data))

