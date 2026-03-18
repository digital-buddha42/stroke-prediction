# Stroke Risk Prediction

A machine learning web app that predicts a patient's stroke risk based on clinical features, built with Flask and scikit-learn.

## Overview

Using a dataset of 5,000+ patient records with 11 clinical features (sourced from Kaggle), we trained a Random Forest classifier to predict stroke likelihood and deployed it as an interactive web application.

**Live app**: https://kevinlad.pythonanywhere.com/

## Model Development

Two models were trained and compared:

| Model | Technique | Notes |
|-------|-----------|-------|
| Model 1 | Random Forest (baseline) | Trained on imbalanced data |
| Model 2 | Random Forest + SMOTE | Synthetic oversampling to address class imbalance |

**Pipeline steps:**
1. Data cleaning — handle missing values, remove outliers
2. Feature engineering — select clinically relevant features
3. Encoding — one-hot encode categorical variables
4. Train/test split + StandardScaler normalization
5. Model training and evaluation (accuracy, classification report)

## Tech Stack

- **ML**: scikit-learn (RandomForestClassifier), imbalanced-learn (SMOTE)
- **Backend**: Flask (Python)
- **Frontend**: HTML/CSS/JavaScript
- **Deployment**: PythonAnywhere

## Files

| File | Description |
|------|-------------|
| `app.py` | Flask app and model integration |
| `project_4_ETL.ipynb` | Data preprocessing pipeline |
| `RandomForestClassifier model.ipynb` | Model training and evaluation |
| `Randomforest.sav` | Serialized trained model |
| `templates/` | HTML templates |
| `static/` | CSS and JavaScript |

## Contributors

[Kevin](https://github.com/Kevin-Lad), [Grace](https://github.com/grace-of-wrath), [Ryan](https://github.com/vasquezr8), [Alec](https://github.com/digital-buddha42), [Mathew](https://github.com/matthewgb26), [Frank](https://github.com/Fpolus)
