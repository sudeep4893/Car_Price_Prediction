from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('rf_model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']
        if Fuel_Type_Petrol == 'Petrol':
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        elif Fuel_Type_Petrol == 'Diesel':
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0
        Year = 2020-Year
        Seller_Type_Individual = request.form['Seller_Type_Individual']
        if Seller_Type_Individual == 'Individual':
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0	
        Transmission_Manual = request.form['Transmission_Manual']
        if Transmission_Manual == 'Mannual':
            Transmission_Manual = 1
        else:
            Transmission_Manual = 0
        # Present_Price, Kms_Driven, Owner, Year, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual
        print(Present_Price) 
        print(Kms_Driven)
        print(Owner)
        print(Year) 
        print(Fuel_Type_Diesel) 
        print(Fuel_Type_Petrol) 
        print(Seller_Type_Individual) 
        print(Transmission_Manual)
        print("----------------------------------------")
        prediction = model.predict([[Present_Price, Kms_Driven, Owner, Year, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
        print("----------------------------------------")
        output = round(prediction[0],2)
        print("Output value is - ",output)
        print("----------------------------------------")
        if output<0:
            return render_template('index.html',prediction_text="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
            
    else:
        return render_template('index.html')

    
if __name__ == "__main__":
    app.run(debug = True)