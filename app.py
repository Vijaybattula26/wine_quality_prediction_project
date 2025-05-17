from flask import Flask, render_template, request
import numpy as np
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the trained model pipeline (ensure this file exists in your project directory)
model = joblib.load('artifacts/model_trainer/model.joblib')

# Home route to render input form
@app.route('/')
def home():
    return render_template('index.html')

# Predict route to handle form submission and show result
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract form values and convert to float
            features = [
                float(request.form['fixed_acidity']),
                float(request.form['volatile_acidity']),
                float(request.form['citric_acid']),
                float(request.form['residual_sugar']),
                float(request.form['chlorides']),
                float(request.form['free_sulfur_dioxide']),
                float(request.form['total_sulfur_dioxide']),
                float(request.form['density']),
                float(request.form['pH']),
                float(request.form['sulphates']),
                float(request.form['alcohol'])
            ]

            # Convert to array and reshape for prediction
            input_data = np.array(features).reshape(1, -1)

            # Predict using the model
            prediction = model.predict(input_data)[0]
            quality_score = round(prediction, 2)

            # Categorize the wine quality and choose color + label
            if quality_score >= 7:
                label = "Good Quality Wine 🍷"
                color = "green"
            elif quality_score >= 5:
                label = "Poor Quality Wine ⚠️"
                color = "orange"
            else:
                label = "Dangerous Wine ❌"
                color = "red"

            # Pass all to template
            return render_template('results.html', 
                                   prediction=f"Predicted Wine Quality: {quality_score}",
                                   label=label,
                                   color=color)

        except Exception as e:
            return render_template('results.html', prediction=f"Error: {str(e)}")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
