import pandas as pd
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)


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

    # Predicted class: 1 for stroke, 0 for no stroke
    return prediction[0]

# This method is called when the app starts running on the server.
@app.route('/')
def index():
    return render_template('index.html')

# This route handles POST requests sent to the server at /predict endpoint. When a POST request is received, it converts the request body into a Python dictionary and passes it to the predict_stroke() function. The function returns a prediction, which is then returned to the client as a response.
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        user_input = request.form.to_dict()
        prediction = predict_stroke(user_input)
        if prediction == 1:
            return "Based on the provided information, you are likely to have a stroke."
        else:
            return "Based on the provided information, you are not likely to have a stroke."

if __name__ == '__main__':
    app.run(debug=True)

