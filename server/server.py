from flask import Flask, request, jsonify
import util
import json
app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    with open("C:\\JAY TALERA\\DATA SCIENCE\\ML PROJECTS\\Banglore-Real-Estate-Price-Prediction\\server\\artifacts\\columns.json", "r") as f:
        response = json.load(f)['data_columns'][3:]
   
    loca = jsonify({
        'locations' : response
    })
    loca.headers.add('Access-Control-Allow-Origin', '*')
    return loca

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Price Prediction.....")
    app.run()