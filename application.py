# import pickle
# from flask import Flask, request, jsonify, render_template
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import StandardScaler
#
# application = Flask(__name__)
# app=application
#
# model = pickle.load(open('lr.pkl', 'rb'))
# scaler = pickle.load(open('sc.pkl', 'rb'))
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/predict',methods=['GET', 'POST'])
# def predict():
#     if request.method == 'POST':
#         Temperature = float(request.form.get('Temperature'))
#         RH = float(request.form.get('RH'))
#         Ws = float(request.form.get('Ws'))
#         Rain = float(request.form.get('Rain'))
#         FFMC = float(request.form.get('FFMC'))
#         DMC = float(request.form.get('DMC'))
#         ISI = float(request.form.get('ISI'))
#         Classes = float(request.form.get('Classes'))
#         Region = float(request.form.get('Region'))
#
#         new_data_scaled = scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
#
#         result = model.predict(new_data_scaled)
#
#         return render_template('home.html', result=result[0])
#
#     else:
#         return render_template('home.html')
#
# if __name__=='__main__':
#     app.run(host='0.0.0.0',port=8080)


import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

application = Flask(__name__)
app = application
CORS(app)  # allow React frontend to access Flask API

model = pickle.load(open('lr.pkl', 'rb'))
scaler = pickle.load(open('sc.pkl', 'rb'))

@app.route('/')
def home():
    return jsonify({"message": "Flask backend is running!"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # JSON input from React
    Temperature = float(data['Temperature'])
    RH = float(data['RH'])
    Ws = float(data['Ws'])
    Rain = float(data['Rain'])
    FFMC = float(data['FFMC'])
    DMC = float(data['DMC'])
    ISI = float(data['ISI'])
    Classes = float(data['Classes'])
    Region = float(data['Region'])

    new_data_scaled = scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
    result = model.predict(new_data_scaled)

    return jsonify({'prediction': float(result[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
