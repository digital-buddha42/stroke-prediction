# import necessary libraries
# from models import create_classes
import os
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, or_
from sqlalchemy.ext.automap import automap_base

import pickle

from flask import (
    Flask,
    render_template,
    request)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# ---------------------------------------------------------
# Web site
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():

    return render_template("data.html")

@app.route("/heart_stroke_prediction")
def stroke():
    return render_template("heart_stroke_prediction.html")

# ---------------------------------------------------------
# Machine Learning inputs


# ---------------------------------------------------------
# API
# ---------------------------------------------------------

# ---------------------------------------------------------
# Datatable

# -------------------------------------------------------------------------------

@app.route("/model", methods=["POST"])
def predict_heart_stroke():
    print('test')
    
    unnamed = 0
    # Get the input values from the form
    Age = float(request.form["age"])

     # hypertension is a binary variable 1 or 0 for either yes or no
    Hypertension = float(request.form["hypertension"])

    # heart disease is a binary variable, 1 for yes, 0 for no
    Heart_Disease = float(request.form["heart-disease"])

    avg_glucose_level = float(request.form["avg_glucose_level"])

    bmi = float(request.form["bmi"])

    # gender is a binary variable 1 o 0 for either male or female
     # Map categorical features to binary values
    gender = request.form["gender"]
    
    Gender_Male = 1 if gender == 'Male' else 0
    Gender_Female = 1 if gender == 'Female' else 0
    Gender_Other = 1 if gender == 'Other' else 0

    ever_married = request.form["ever-married"]

    ever_married_yes = 1 if ever_married == 'Yes' else 0
    ever_married_no = 1 if ever_married == 'No' else 0

    work_type = request.form["work-type"]
    
    work_type_children = 1 if work_type == 'children' else 0
    work_type_government_job = 1 if work_type == 'government-job' else 0
    work_type_never_worked = 1 if work_type == 'never-worked' else 0
    work_type_private = 1 if work_type == 'private' else 0
    work_type_self_employed = 1 if work_type == 'self-employed' else 0

    residence_type = (request.form["residence-type"])

    residence_type_rural = 1 if residence_type == 'rural' else 0
    residence_type_urban = 1 if residence_type == 'urban' else 0

    if residence_type_rural == 1:
        residence_type_urban = 0

    # smoking status is a binary variable 1 or 0 for either yes or no
    smoking_status = (request.form["smoking_status"])

    smoking_status_formerly_smoked = 1 if smoking_status == 'formerly-smoked' else 0
    smoking_status_never_smoked = 1 if smoking_status == 'never-smoked' else 0
    smoking_status_smokes = 1 if smoking_status == 'smokes' else 0
    smoking_status_unknown = 1 if smoking_status == 'unknown' else 0

   

    # Create a feature vector for prediction
    X = [[unnamed, Age, Hypertension, Heart_Disease, avg_glucose_level, bmi, Gender_Female, Gender_Male, Gender_Other, 
        ever_married_no, ever_married_yes, work_type_never_worked, work_type_private, work_type_government_job, 
        work_type_self_employed, work_type_children, 
        residence_type_rural, residence_type_urban, smoking_status_formerly_smoked, smoking_status_never_smoked, 
        smoking_status_smokes, smoking_status_unknown]]
    
    print(X)

    # Load the trained heart stroke prediction model
    filename = './models/Randomforest.sav' # Replace model with actual file name
    loaded_model = pickle.load(open(filename, 'rb'))

  
    # Make the prediction
    prediction = loaded_model.predict(X)[0]

    prediction = "{0:,.2f}".format(prediction)

    print(prediction)
 

    return render_template("heart_stroke_prediction.html", prediction=prediction)

if __name__ == "__main__":
    app.run()
