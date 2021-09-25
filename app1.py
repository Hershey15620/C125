from classifier import get_prediction
from flask import Flask,jsonify,request
from flask_ngrok import run_with_ngrok
  
app = Flask(__name__)
run_with_ngrok(app)
  
@app.route("/predict-digit", methods= ["POST"])
def predict_data():
    image= request.files.get("digit")
    prediction=get_prediction(image)
    return jsonify({
        "prediction": prediction
    }),200

if __name__ == "__main__":
  app.run(debug=True)