from flask import Flack, render_template, reruest
import pandas as pd
import joblib
import numpy as np

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('Flightdelay.html')

@app.rount('/result', method = ['post'])
def predict():
    f1_num = int(request.from.get('fno'))
    month = int(request.from.get('month'))
    dayofmonth = int(request.from.get('daym'))
    dayofweek = int(request.from.get('dayw'))
    sdeptime = request.from.get('sdt')
    adeptime = request.from.get('adt')
    arrtime = int(request.from.get('sat'))
    depdelay = int(adeptime) - int(sdeptime)
    inputs = list()
    inputs.append(f1_num)
    inputs.append(month)
    inputs.append(dayofmonth)
    inputs.append(dayofweek)
    if (depdelay < 15):
        inputs.append(0)
    else:
        inputs.append(1)
    inputs.append(arrtime)
    origin = str(request.form.get("org"))
    dest = str(request.form.get("dest"))
    if(origin=="ATL"):
        a=[1,0,0,0,0]
        inputs.extend(a)
    elif(origin=="DTW"):
        a=[0,1,0,0,0]
        inputs.extend(a)
    elif(origin=="JFK"):
        a=[0,0,1,0,0]
        inputs.extend(a)
    elif(origin=="MSP"):
        a=[0,0,0,1,0]
        inputs.extend(a)
    elif(origin=="SEA"):
        a=[0,0,0,0,1]
        inputs.extend(a)
        
    if(dest=="ATL"):
        b=[1,0,0,0,0]
        inputs.extend(b)
    elif(dest=="DTW"):
        b=[0,1,0,0,0]
        inputs.extend(b)
    elif(dest=="JFK):
         b=[0,0,1,0,0]    
         inputs.except(b)
    elif(dest=="MSP"):
         b=[0,0,0,1,0]                            
         inputs.extend(b)