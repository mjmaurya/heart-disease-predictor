from flask import Flask
from flask import render_template,redirect,request
import pandas as pd
import sys
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_log_error
from sklearn.linear_model import LogisticRegression


df=pd.read_csv('heart-data.csv')
df.rename(columns={"class":"target"},inplace=True)
df['target'].replace(['absent','present'],[0,1],inplace=True)
df=pd.get_dummies(df)
x=df.drop('target', axis=1)
y=df['target']
train_x,valid_x,train_y,valid_y=train_test_split(x,y,test_size=0.3,random_state=35)
logr=LogisticRegression()
logr.fit(train_x,train_y)
#new_data=np.array(new_data,dtype='int64')
#new_data=new_data.reshape(1,13)
#xnew_data=pd.DataFrame(new_data)
pickle.dump(logr,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
result=model.predict(valid_x)
newdata=valid_x.head(1)
print(newdata)
result2=model.predict(newdata)
print(result)
print(result2)
    

