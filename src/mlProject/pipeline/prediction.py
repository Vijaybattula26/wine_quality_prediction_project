import numpy as np
import joblib
import os

class PredictionPipeline:
    def __init__(self):
        model_path = os.path.join("artifacts", "model_trainer", "model.joblib")
        self.model = joblib.load(model_path)

    def predict(self, features):
        # Ensure features is a list or array of floats in correct order
        features_array = np.array([features])
        prediction = self.model.predict(features_array)
        # Return rounded float prediction to 2 decimal places
        return round(float(prediction[0]), 2)