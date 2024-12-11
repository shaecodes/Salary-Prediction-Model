from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('salary_predictor.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict([data['features']])
    return jsonify({'salary': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
