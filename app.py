from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load("churn_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    # Parse JSON input
    data = request.get_json()
    df = pd.DataFrame([data])

    # Predict churn probability
    prediction = model.predict(df)
    probability = model.predict_proba(df)[:, 1]

    return jsonify({
        "prediction": int(prediction[0]),
        "probability": float(probability[0])
    })

if __name__ == '__main__':
    app.run(debug=True)
