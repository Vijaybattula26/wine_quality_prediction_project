import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'mlProject', 'pipeline'))

from flask import Flask, render_template, request, flash
import numpy as np
from prediction import PredictionPipeline  # import your pipeline class

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Important for flash messages

# Initialize PredictionPipeline instance once
pipeline = PredictionPipeline()

FEATURE_RANGES = {
    "fixed_acidity": (4.0, 16.0),
    "volatile_acidity": (0.1, 1.5),
    "citric_acid": (0.0, 1.0),
    "residual_sugar": (0.5, 15.0),
    "chlorides": (0.01, 0.2),
    "free_sulfur_dioxide": (1, 72),
    "total_sulfur_dioxide": (6, 289),
    "density": (0.9900, 1.005),
    "pH": (2.5, 4.5),
    "sulphates": (0.3, 2.0),
    "alcohol": (8.0, 15.0)
}

# Store prediction history (limited to last 10)
prediction_history = []

@app.route('/')
def index():
    # Prepare features list for the template
    features_for_template = [(feature, min_val, max_val) for feature, (min_val, max_val) in FEATURE_RANGES.items()]
    return render_template('index.html', features=features_for_template, prediction=None, history=prediction_history, inputs={})

@app.route('/predict', methods=['POST'])
def predict():
    inputs = {}
    prediction = None
    label = ""
    color = ""
    try:
        input_features = []
        # Validate and collect inputs
        for feature, (min_val, max_val) in FEATURE_RANGES.items():
            val_str = request.form.get(feature)
            if val_str is None or val_str.strip() == '':
                raise ValueError(f"Input for '{feature}' is missing.")

            val = float(val_str)

            if not (min_val <= val <= max_val):
                raise ValueError(f"'{feature}' must be between {min_val} and {max_val}. You entered {val}.")

            inputs[feature] = val
            input_features.append(val)

        # Call predict with a 1D list (not nested list)
        quality_score = pipeline.predict(input_features)
        prediction = quality_score

        # Generate label and color based on quality score
        if quality_score >= 6.5:
            label = "Good Quality Wine 🍷"
            color = "green"
        elif quality_score >= 4.5:
            label = "Poor Quality Wine ⚠️"
            color = "orange"
        else:
            label = "Dangerous Wine ❌"
            color = "red"

        # Add this prediction to the history list, newest first
        prediction_history.insert(0, {
            "inputs": inputs,
            "prediction": quality_score,
            "label": label,
            "color": color
        })

        # Limit history size to last 10 predictions
        if len(prediction_history) > 10:
            prediction_history.pop()

        print(f"Predicted Score: {quality_score}, Label: {label}") # Debugging output

        # Prepare features list for the template
        features_for_template = [(feature, min_val, max_val) for feature, (min_val, max_val) in FEATURE_RANGES.items()]
        # Render index.html with results and history
        return render_template(
            'index.html',
            features=features_for_template,
            inputs=inputs,
            prediction=prediction,
            label=label,
            color=color,
            history=prediction_history
        )

    except ValueError as ve:
        app.logger.error(f"Validation error: {ve}")
        flash(str(ve), 'error')
        # Prepare features list for the template
        features_for_template = [(feature, min_val, max_val) for feature, (min_val, max_val) in FEATURE_RANGES.items()]
        return render_template(
            'index.html',
            features=features_for_template,
            inputs=request.form.to_dict(), # Pass back the form data to repopulate fields
            prediction=None,
            history=prediction_history
        )
    except Exception as e:
        app.logger.error(f"Prediction error: {e}")
        flash(f"An unexpected error occurred: {e}", 'error')
        # Prepare features list for the template
        features_for_template = [(feature, min_val, max_val) for feature, (min_val, max_val) in FEATURE_RANGES.items()]
        return render_template(
            'index.html',
            features=features_for_template,
            inputs=request.form.to_dict(), # Pass back the form data to repopulate fields
            prediction=None,
            history=prediction_history
        )

if __name__ == '__main__':
    app.run(debug=True)