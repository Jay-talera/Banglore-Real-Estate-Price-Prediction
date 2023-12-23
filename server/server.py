from flask import Flask, request, jsonify
import json
import numpy as np
import pickle
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return 'Welcome To Banglore Price Prediction WEB-APP By :Jay Jain'

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    with open("C:\\JAY TALERA\\DATA SCIENCE\\ML PROJECTS\\Banglore-Real-Estate-Price-Prediction\\server\\artifacts\\columns.json", "r") as f:
        response = json.load(f)['data_columns'][3:]
   
    response = jsonify({
        'locations' : response
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    with open("C:\\JAY TALERA\\DATA SCIENCE\\ML PROJECTS\\Banglore-Real-Estate-Price-Prediction\\server\\artifacts\\columns.json", "r") as f:
        data_columns = json.load(f)['data_columns']
        locations = data_columns[3:]
    model = None
    if model is None:
        with open('C:\\JAY TALERA\\DATA SCIENCE\\ML PROJECTS\\Banglore-Real-Estate-Price-Prediction\\server\\artifacts\\banglore_home_prices_model.pickle', 'rb') as f:
            model = pickle.load(f)
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    est_price = round(model.predict([x])[0],2)
    response = jsonify({
        'estimated_price': est_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Price Prediction.....")
    app.run()