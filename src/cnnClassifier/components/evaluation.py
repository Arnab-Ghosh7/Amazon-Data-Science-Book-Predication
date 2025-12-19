import pandas as pd
import joblib
from pathlib import Path
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


class Evaluation:
    def __init__(self, config):
        self.config = config
        self.eval_dir = Path("artifacts/evaluation")
        self.eval_dir.mkdir(parents=True, exist_ok=True)

    def evaluate(self):
        # Load trained model
        model = joblib.load(self.config.model_path)

        # Load dataset
        df = pd.read_csv(self.config.training_data)

        X = df.iloc[:, 0].astype(str)
        y = df.iloc[:, -1]

        y_pred = model.predict(X)

        # -------- Metrics --------
        accuracy = accuracy_score(y, y_pred)
        precision = precision_score(
            y, y_pred, average="weighted", zero_division=0
        )
        recall = recall_score(
            y, y_pred, average="weighted", zero_division=0
        )
        f1 = f1_score(
            y, y_pred, average="weighted", zero_division=0
        )

        # -------- Print --------
        print("\n📊 Evaluation Metrics")
        print("Accuracy :", accuracy)
        print("Precision:", precision)
        print("Recall   :", recall)
        print("F1-score :", f1)

        report = classification_report(
            y, y_pred, zero_division=0
        )
        cm = confusion_matrix(y, y_pred)

        print("\n📄 Classification Report")
        print(report)

        print("\n🧩 Confusion Matrix")
        print(cm)

        # -------- Save to artifacts --------
        self._save_metrics(accuracy, precision, recall, f1)
        self._save_report(report)
        self._save_confusion_matrix(cm)

    def _save_metrics(self, accuracy, precision, recall, f1):
        with open(self.eval_dir / "metrics.txt", "w") as f:
            f.write(f"Accuracy  : {accuracy}\n")
            f.write(f"Precision : {precision}\n")
            f.write(f"Recall    : {recall}\n")
            f.write(f"F1-score  : {f1}\n")

    def _save_report(self, report: str):
        with open(self.eval_dir / "classification_report.txt", "w", encoding="utf-8") as f:
            f.write(report)

    def _save_confusion_matrix(self, cm):
        with open(self.eval_dir / "confusion_matrix.txt", "w") as f:
            f.write(str(cm))
