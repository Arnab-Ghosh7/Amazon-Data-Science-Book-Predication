### 🔧 Built With

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![NLP](https://img.shields.io/badge/NLP-Text%20Classification-green)
![Model](https://img.shields.io/badge/Model-TF--IDF%20%2B%20LogReg-orange)
![Backend](https://img.shields.io/badge/Backend-Flask-black)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

# 📚 Amazon Data Science Book Classification

A complete end-to-end NLP machine learning project that classifies Amazon Data Science books using TF-IDF features and Logistic Regression, wrapped inside a production-ready pipeline with training, evaluation, and a Flask web application for real-time predictions.

---

## 🚀 Project Overview

This project is a full-stack Natural Language Processing (NLP) machine learning application designed to automatically classify Amazon Data Science–related books based on textual information such as book titles or descriptions.

The goal of the project is to demonstrate how a real-world text classification system can be built using classical machine learning techniques while following production-level software engineering practices. Rather than focusing only on model accuracy, the project emphasizes clean architecture, modular design, reproducibility, and deployability, which are critical in industry environments.

At its core, the system converts raw text into numerical representations using TF-IDF (Term Frequency–Inverse Document Frequency), capturing both the importance of words and their contextual relevance. These features are then fed into a Logistic Regression classifier, a strong and interpretable baseline model widely used for large-scale text classification tasks.

The entire workflow is structured as a pipeline consisting of clearly separated stages:

- Data ingestion from a structured CSV source

- Model training using configurable hyperparameters

- Model evaluation with comprehensive performance metrics

- Real-time inference through a RESTful API

To make the project end-user accessible, a Flask web application is integrated, allowing users to input text and receive predictions instantly. All intermediate outputs—including trained models, logs, and evaluation reports—are stored as versioned artifacts, ensuring traceability and reproducibility.

---

## Tech Stack
- Programming Language: Python

- Machine Learning:

- TF-IDF Vectorizer

- Logistic Regression (Scikit-learn)

- Backend: Flask

- Pipeline Management: Custom modular pipeline

- Model Persistence: Joblib

- Configuration: YAML

- Frontend: HTML + Bootstrap

- Deployment Ready: Yes 

---

## 📂 Project Structure

<pre>
Amazon-Data-Science-Book/
│
├── app.py                         # Flask application
├── main.py                        # Pipeline runner
├── setup.py                       # Package setup
├── params.yaml                    # Model & training parameters
├── config.yaml                    # Pipeline configuration
│
├── artifacts/
│   ├── data_ingestion/            # Raw & processed data
│   ├── training/                  # Trained model
│   └── evaluation/                # Evaluation reports
│
├── src/
│   └── cnnClassifier/
│       ├── components/
│       │   ├── data_ingestion.py
│       │   ├── training.py
│       │   ├── evaluation.py
│       │   └── prediction.py
│       │
│       ├── config/
│       │   └── configuration.py
│       │
│       ├── entity/
│       │   └── config_entity.py
│       │
│       ├── pipeline/
│       │   ├── stage_01_data_ingestion.py
│       │   ├── stage_03_training.py
│       │   └── stage_04_evaluation.py
│       │
│       ├── utils/
│       │   └── common.py
│       │
│       └── __init__.py
│
├── templates/
│   └── index.html                 # Web UI
│
└── logs/
    └── running_logs.log

</pre>

---

## DVC Pipeline Stages

1. Data Ingestion  
2. Model Training  
3. Model Evaluation  

Run the full pipeline:
<pre>dvc repro</pre>

## Clone the Repository

```text
git clone https://github.com/Arnab-Ghosh7/Amazon-Data-Science-Book-Predication.git
cd Amazon-Data-Science-Book-Predication
```
## Create Environment & Install Dependencies

```text
conda create -n nlp_env python=3.10 -y
conda activate nlp_env
pip install -r requirements.txt
```

### Train the Model
```
python main.py
```

### Run Flask App
```
python app.py
```
### Open in browser:
```
http://127.0.0.1:5000/
```

---

## Model Output

The model predicts whether the chicken fecal image belongs to:
- Accuracy

- Precision (weighted)

- Recall (weighted)

- F1-Score

- Full classification report

Evaluation metrics are stored in - artifacts/evaluation/



---

## Author

Arnab Ghosh  

GitHub: https://github.com/Arnab-Ghosh7

---

## License

This project is licensed under the MIT License.


