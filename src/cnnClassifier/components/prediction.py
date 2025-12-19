import joblib
from pathlib import Path


class Prediction:
    def __init__(self, model_path: Path):
        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self):
        return joblib.load(self.model_path)

    def predict(self, text: str):
        """
        Predict class for a single text input
        """
        prediction = self.model.predict([text])
        return prediction[0]

    def predict_batch(self, texts: list):
        """
        Predict classes for multiple text inputs
        """
        return self.model.predict(texts)
