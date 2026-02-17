from flask import Flask, render_template, request
import pandas as pd
from utils import load_models, make_prediction

# Initializing Flask App
app = Flask(__name__)

# Load models once at startup
tabular_model, text_model, meta_model = load_models()
models = (tabular_model, text_model, meta_model)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extracting features from form
        data = {
            'age': [int(request.form['age'])],
            'sex': [request.form['sex']],
            'race': [request.form['race']],
            'priors_count': [int(request.form['priors_count'])],
            'juv_fel_count': [int(request.form['juv_fel_count'])],
            'juv_misd_count': [int(request.form['juv_misd_count'])],
            'juv_other_count': [int(request.form['juv_other_count'])],
            'c_charge_degree': [request.form['c_charge_degree']],
            'c_charge_desc': [request.form['c_charge_desc']],
            'days_b_screening_arrest': [float(request.form.get('days_b_screening_arrest', 0))],
            'c_days_from_compas': [float(request.form.get('c_days_from_compas', 0))]
        }
        
        score, risk_level, risk_class, confidence, bias_message = make_prediction(models, data)

        return render_template('result.html', score=score, risk_level=risk_level, risk_class=risk_class, confidence=confidence, bias_message=bias_message)

    except Exception as e:
        return f"An error occurred during prediction: {e}"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
