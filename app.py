from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route('/')
def home():
    return "Hello World!"

@app.route('/your_name')
def your_name():
    return "To jest moja strona"

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get("name", "")
    if name:
        return f"Hello {name}"
    else:
        return "Hello"

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    x1 = request.args.get("x1", 0, type=float)
    x2 = request.args.get("x2", 0, type=float)

    prediction = model.predict(np.array([[x1, x2]]))

    prediction = int(prediction[0])

    features = {
        "x1": x1,
        "x2": x2
    }

    response = {
        "prediction": prediction,
        "features": features
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

