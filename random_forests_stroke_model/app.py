import pandas as pd
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

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


# Loading the pre-trained model and making predictions on the input data.
# Function to predict stroke likelihood
def predict_stroke(data):
    print("Received keys:", data.keys())
    # Load the saved model
    filename = 'Randomforest.sav'
    with open(filename, 'rb') as model_file:
        model = pickle.load(model_file)

    # Prepare the input data as a DataFrame
    input_data = pd.DataFrame({
        'Gender': [data['gender']],  
        'Age': [data['age']],
        'Average Glucose Level': [data['avgGlucoseLevel']],
        'BMI': [data['bmi']],
        'Hypertension': [data['hypertension']],
        'Heart Disease': [data['heartDisease']],
        'Ever Married': [data['everMarried']],
        'Work Type': [data['workType']],
        'Residence Type': [data['residenceType']],
        'Smoking Status': [data['smokingStatus']]
    })


    # Convert categoricals to one-hot encoded dummy variables
    # Make predictions
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    # Predicted class: 1 for stroke, 0 for no stroke
    print(probability[0][1])
    return prediction[0], probability[0][1]
    

# This method is called when the app starts running on the server.
@app.route('/')
def index():
    return render_template('index.html')

# This route handles POST requests sent to the server at /predict endpoint. When a POST request is received, it converts the request body into a Python dictionary and passes it to the predict_stroke() function. The function returns a prediction, which is then returned to the client as a response.
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        user_input = request.form.to_dict()
        prediction, probability = predict_stroke(user_input)
        
        if prediction == 1:
            return f"Based on the provided information, you are likely to have a stroke. The probability of having a stroke is {100*round(probability,2)}%"
        else:
            return f"Based on the provided information, you are not likely to have a stroke. The probability of having a stroke is {100*round(probability,2)}%"

if __name__ == '__main__':
    app.run(debug=True)

