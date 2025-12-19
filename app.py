from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pathlib import Path
import os

from cnnClassifier.components.prediction import Prediction
from cnnClassifier import logger




os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.model_path = Path("artifacts/training/model.h5")
        self.predictor = Prediction(model_path=self.model_path)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/train", methods=["GET", "POST"])
def train_route():
    os.system("python main.py")
    return jsonify({"message": "Training completed successfully"})


@app.route("/predict", methods=["POST"])
def predict_route():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Please provide 'text' field"}), 400

    text = data["text"]

    prediction = clApp.predictor.predict(text)

    return jsonify({
        "input_text": text,
        "prediction": prediction
    })


if __name__ == "__main__":
    clApp = ClientApp()

    # Local
    app.run(host="0.0.0.0", port=8080, debug=True)

