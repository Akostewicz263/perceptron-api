# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():

    x1 = request.args.get("x1", 0, type=float)
    x2 = request.args.get("x2", 0, type=float)
    

    input_data = np.array([[x1, x2]])
    

    prediction = model.predict(input_data)[0]
    
    
    response = {
        "features": {"x1": x1, "x2": x2},
        "predicted_class": prediction
    }
    
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
