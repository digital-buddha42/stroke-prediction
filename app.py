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
    jsonify,
    request,
    redirect)

engine = create_engine("sqlite:///data/movies.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
print(Base.classes.keys())

Movies = Base.classes.movies
Actors = Base.classes.actors

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
@app.route("/api/movies")
def movie_grid():

    session = Session(engine)

    results = session.query(Movies.title, Movies.director, Movies.year, Movies.rating, Movies.imdb_votes, Movies.imdb_score).all()

    results = [list(r) for r in results]

    table_results = {
        "table": results
    }

    session.close()

    return jsonify(table_results)

# -------------------------------------------------------------------------------
# Charts
@app.route("/api/years/<year>")
def years(year):

    session = Session(engine)

    if year == "before":
        results = session.query(Movies.title, Movies.director, Movies.year, 
            Movies.rating, Movies.imdb_votes, Movies.imdb_score).filter(Movies.year < 2000).all()
    else:
        results = session.query(Movies.title, Movies.director, Movies.year, 
            Movies.rating, Movies.imdb_votes, Movies.imdb_score).filter(Movies.year >= 2000).all()

    results = [list(r) for r in results]

    rating = [result[3] for result in results]
    votes = [result[4] for result in results]

    year_results = {
        "rating": rating,
        "votes": votes,
    }

    session.close()

    return jsonify(year_results)


@app.route("/api/directors/<director>")
def directors(director):

    print(director)

    if director == "chaplin":
        name = "Charles Chaplin"
    elif director == "hitchcock":
        name = "Alfred Hitchcock"
    elif director == "nolan":
        name = "Christopher Nolan"
    else:
        name = "Akira Kurosawa"

    session = Session(engine)

    G_results = session.query(func.avg(Movies.imdb_score)).filter(Movies.rating=="G").filter(Movies.director == name).all()
    PG_results = session.query(func.avg(Movies.imdb_score)).filter(Movies.rating=="PG").filter(Movies.director == name).all()
    PG_plus_results = session.query(func.avg(Movies.imdb_score)).filter(or_(Movies.rating=="PG+", Movies.rating=="PG-13")).filter(Movies.director == name).all()
    R_results = session.query(func.avg(Movies.imdb_score)).filter(Movies.rating=="R").filter(Movies.director == name).all()
    Other_results = session.query(func.avg(Movies.imdb_score)).filter(or_(Movies.rating=="APPROVED",Movies.rating=="NOT RATED", Movies.rating=="N\A", Movies.rating=="PASSED")).filter(Movies.director == name).all()

    results = [G_results[0][0], PG_results[0][0], PG_plus_results[0][0], R_results[0][0], Other_results[0][0]]
    labels = ["G", "PG", "PG+", "R", "Other"]

    director_results = {
        "labels": labels,
        "scores": results,
    }

    session.close()

    return jsonify(director_results)

@app.route("/model", methods=["POST"])
def predict_heart_stroke():

    # Get the input values from the form
    age = float(request.form["age"])

     # hypertension is a binary variable 1 or 0 for either yes or no
    hypertension = float(request.form["hypertension"])

    # heart disease is a binary variable, 1 for yes, 0 for no
    heart_disease = float(request.form["heart-disease"])

    avg_glucose_level = float(request.form["avg_glucose_level"])

    bmi = float(request.form["bmi"])

    # gender is a binary variable 1 o 0 for either male or female
     # Map categorical features to binary values
    gender = request.form["gender"]
    
    gender_m = float(1 if gender == 'Male' else 0)
    gender_f = float(1 if gender == 'Female' else 0)
    gender_o = float(1 if gender == 'Other' else 0)

    ever_married = request.form["ever-married"]

    ever_married_yes = float(1 if ever_married == 'yes' else 0)
    ever_married_no = float(1 if ever_married == 'no' else 0)

    work_type = request.form["work-type"]
    
    work_type_children = float(1 if work_type == 'children' else 0)
    work_type_government_job = float(1 if work_type == 'government-job' else 0)
    work_type_never_worked = float(1 if work_type == 'never-worked' else 0)
    work_type_private = float(1 if work_type == 'private' else 0)
    work_type_self_employed = float(1 if work_type == 'self-employed' else 0)

    residence_type = (request.form["residence-type"])

    residence_type_rural = float(1 if residence_type == 'rural' else 0)
    residence_type_urban = float(1 if residence_type == 'urban' else 0)


    # smoking status is a binary variable 1 or 0 for either yes or no
    smoking_status = (request.form["smoking_status"])

    smoking_status_formerly_smoked = float(1 if smoking_status == 'formerly-smoked' else 0)
    smoking_status_never_smoked = float(1 if smoking_status == 'never-smoked' else 0)
    smoking_status_smokes = float(1 if smoking_status == 'smokes' else 0)
    smoking_status_unknown = float(1 if smoking_status == 'unknown' else 0)

   
    # prediction = 0 

    # Create a feature vector for prediction
    X = [[age, hypertension, heart_disease, avg_glucose_level, bmi, gender_f, gender_m, gender_o, 
        ever_married_no, ever_married_yes, work_type_government_job, work_type_never_worked, work_type_private, 
        work_type_self_employed, work_type_children, 
        residence_type_rural, residence_type_urban, smoking_status_formerly_smoked, smoking_status_never_smoked, 
        smoking_status_smokes, smoking_status_unknown]]
    
    print(X)
    print(len(X[0]))


    # Load the trained heart stroke prediction model
    filename = './models/svm_model (3).sav' # Replace model with actual file name
    loaded_model = pickle.load(open(filename, 'rb'))

    # Load the trained heart stroke prediction model
    filename = './models/svm__scalar_model.sav' # Replace model with actual file name
    X_Scaler = pickle.load(open(filename, 'rb'))

    X_scaled = X_Scaler.transform(X)

    # Make the prediction
    prediction = loaded_model.predict(X_scaled)[0]

    prediction = "{0:,.2f}".format(prediction)

    print(prediction)
 

    return render_template("heart_stroke_prediction.html", prediction=prediction)

if __name__ == "__main__":
    app.run()
