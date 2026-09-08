from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load saved ML files
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")
label_encoders = joblib.load("label_encoders.pkl")


@app.route("/")
def home():
    return jsonify({
        "message": "Vehicle Fuel Efficiency Prediction API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    new_data = pd.DataFrame([data])

    # Encode categorical features
    for column, encoder in label_encoders.items():
        new_data[column] = encoder.transform(new_data[column])

    # Keep the correct feature order
    new_data = new_data[feature_names]

    # Apply scaling
    new_data = scaler.transform(new_data)

    # Make prediction
    prediction = model.predict(new_data)

    return jsonify({
        "predicted_mpg": float(prediction[0])
    })
