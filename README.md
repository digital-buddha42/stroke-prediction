# stroke-prediction
# Stroke Risk Prediction Web App:
https://kevinlad.pythonanywhere.com/

## Table of Contents
- [Contributors](#contributors)
- [Overview](#overview)
- [Files](#files)
  - [Web App](#web-app)
  - [Machine Learning Model](#machine-learning-model)
- [Dataset Preparation](#dataset-preparation)
- [Model Development](#model-development)
- [Model Evaluation](#model-evaluation)
## Contributors
- [Kevin](https://github.com/Kevin-Lad)
- [Grace](https://github.com/grace-of-wrath)
- [Ryan](https://github.com/vasquezr8)
- [Alec](https://github.com/digital-buddha42)
- [Mathew](https://github.com/matthewgb26)
- [Frank](https://github.com/Fpolus)
## Overview
The stroke risk prediction web app is a comprehensive project built using Flask, integrating a machine learning model trained on a carefully curated dataset to predict the likelihood of a stroke for a given set of input parameters. The team collected and utilized data from a public dataset available on [Kaggle](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/), encompassing over 5,000 records with 11 clinical features that play crucial roles in predicting stroke events.
## Files
### Web App
The core files for the web app include:
- `app.py`: This file contains the Flask routes and integration of the machine learning model.
- `templates/`: This directory holds HTML templates used for rendering the web pages.
- `static/`: Contains CSS and JavaScript files, enhancing the user interface with styling and interactivity.
### Machine Learning Model
The heart of this project lies in the machine learning model designed to predict stroke risk. The team utilized a Jupyter Notebook named `stroke_prediction_model.ipynb` to meticulously develop and fine-tune this model using Python.
#### Development Process
1. **Data Preprocessing**: The dataset underwent thorough cleaning, handling missing values, and addressing outliers. Feature engineering techniques were employed to enhance the predictive capability of the model.
2. **Feature Selection**: A comprehensive analysis was conducted to select the most influential features affecting stroke occurrence.
3. **Encoding Categorical Variables**: Categorical variables were encoded appropriately for machine learning algorithms.
4. **Data Splitting**: The dataset was split into training and testing sets to evaluate the model's performance on unseen data.
#### Model Selection and Training
Two models were trained using the Random Forest classifier:
- **Model 1**: Trained without Synthetic Minority Over-sampling Technique (SMOTE).
- **Model 2**: Utilized SMOTE to address class imbalance effectively.
#### Evaluation and Insights
Both models underwent rigorous evaluation against the test set, measuring their performance using accuracy and classification reports.
## Dataset Preparation
The Jupyter Notebook details the meticulous steps taken to prepare the dataset for training. These steps include comprehensive data cleaning, thoughtful feature selection, careful encoding of categorical variables, and strategic data splitting.
## Model Development
The team employed the Random Forest classifier as the model of choice for predicting stroke risk. Two models were trained:
- One model was trained without Synthetic Minority Over-sampling Technique (SMOTE).
- Another model was trained leveraging SMOTE to handle class imbalance effectively.
## Model Evaluation
Both models underwent rigorous evaluation based on the test set. Their performance was measured in terms of accuracy and other metrics detailed in the classification report.
Your contributions to this project are highly valued! Feel free to explore the codebase and contribute to further enhancements. If you have any questions or feedback, please don't hesitate to reach out to the contributors.