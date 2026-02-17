import joblib
import pandas as pd
import numpy as np
import os

MODEL_DIR = 'models'

def load_models():
    """Load the trained models from disk."""
    try:
        tabular_model = joblib.load(os.path.join(MODEL_DIR, 'tabular_model.pkl'))
        text_model = joblib.load(os.path.join(MODEL_DIR, 'text_model.pkl'))
        meta_model = joblib.load(os.path.join(MODEL_DIR, 'meta_model.pkl'))
        return tabular_model, text_model, meta_model
    except Exception as e:
        print(f"Error loading models: {e}")
        return None, None, None

def make_prediction(models, data):
    """
    Make a prediction using the ensemble of models.
    
    Args:
        models: Tuple of (tabular_model, text_model, meta_model)
        data: Dictionary of input features
        
    Returns:
        tuple: (score, risk_level, risk_class, confidence)
    """
    tabular_model, text_model, meta_model = models
    
    # Create DataFrame
    X_input = pd.DataFrame(data)
    
    # Generate Predictions (Probabilities)
    # 1. Tabular Model Probs
    tab_probs = tabular_model.predict_proba(X_input)
    
    # 2. Text Model Probs
    text_probs = text_model.predict_proba(X_input['c_charge_desc'].astype(str))
    
    # 3. Meta Features
    meta_features = np.hstack((tab_probs, text_probs))
    
    # 4. Final Prediction
    # Get probabilities for each decile (1-10)
    meta_probs = meta_model.predict_proba(meta_features)[0]
    
    # Get the class with highest probability
    # Classes are likely [1, 2, ..., 10]
    # argmax gives index 0..9
    prediction_idx = np.argmax(meta_probs)
    score = tabular_model.classes_[prediction_idx] # Accurately map index to class label
    
    # Determine visual feedback and aggregate confidence
    risk_level = "Low"
    risk_class = "low-risk"
    confidence = 0.0
    
    # Sum probabilities for the relevant risk buckets
    # Assuming classes are sorted 1..10
    
    if score <= 4:
        risk_level = "Low"
        risk_class = "low-risk"
        # Low risk: 1-4 (Indices 0, 1, 2, 3)
        confidence = np.sum(meta_probs[0:4])
        
    elif score <= 7:
        risk_level = "Medium"
        risk_class = "medium-risk"
        # Medium risk: 5-7 (Indices 4, 5, 6)
        confidence = np.sum(meta_probs[4:7])
        
    else:
        risk_level = "High"
        risk_class = "high-risk"
        # High risk: 8-10 (Indices 7, 8, 9)
        confidence = np.sum(meta_probs[7:10])

    # Bias Warning Logic
    bias_message = None
    input_race = data.get('race', [''])[0]
    if input_race in ['African-American', 'Native American']:
        bias_message = (
            f"Caution: The model has historically shown high False Positive Rates for "
            f"{input_race} defendants. This risk score may be inflated due to systemic biases "
            f"in the training data."
        )

    return int(score), risk_level, risk_class, round(confidence * 100, 1), bias_message
