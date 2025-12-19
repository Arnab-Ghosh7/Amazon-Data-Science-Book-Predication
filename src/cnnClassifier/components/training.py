import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


class Training:
    def __init__(self, config):
        self.config = config

    def train(self):
        # Load CSV
        df = pd.read_csv(self.config.training_data)

        # DEBUG: show columns once
        print("CSV columns:", df.columns.tolist())

        # ✅ SAFE SELECTION (NO COLUMN NAMES)
        X = df.iloc[:, 0].astype(str)   # first column → text
        y = df.iloc[:, -1]              # last column → label

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
        )

        model = Pipeline([
            ("tfidf", TfidfVectorizer(
                max_features=self.config.max_features,
                ngram_range=self.config.ngram_range
            )),
            ("clf", LogisticRegression(max_iter=1000))
        ])

        model.fit(X_train, y_train)

        joblib.dump(model, self.config.trained_model_path)

        print("✅ Model trained and saved successfully")
