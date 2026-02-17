# AI Justice Assistant | Recidivism Risk Assessment

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-orange.svg)

## 📌 Project Overview

**AI Justice Assistant** is a machine learning-powered web application designed to assist legal professionals in assessing recidivism risk (the likelihood of a criminal defendant re-offending).

This project replicates and enhances the critical analysis of the **COMPAS** algorithm. It features a transparent, interpretable model that combines tabular defendant data with natural language processing (NLP) of charge descriptions to provide a holistic risk assessment.

### 🚀 Key Features
- **Hybrid AI Model**: Combines Logistic Regression (Tabular data) and TF-IDF/Naive Bayes (Text data) via a Meta-Learner.
- **Glass-Box Design**: Prioritizes interpretability to reduce "black box" dangers in judicial AI.
- **Model Confidence Score**: Displays the model's prediction probability to provide transparency on certainty.
- **Bias Warning System**: Automatically flags potential algorithmic bias for demographic groups with historically high error rates.
- **Modern UI/UX**: Features a responsive, glassmorphism interface for a seamless user experience.
- **Ethical AI Focus**: Built with fairness constraints and bias awareness as core principles.

---

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, joblib, pandas, numpy
- **Frontend**: HTML5, CSS3 (Glassmorphism design), Google Fonts
- **Data**: COMPAS Recidivism Racial Bias Dataset

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/kidou16/AAIFinal.git
   cd AAIFinal
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Access the App**
   Open your browser and navigate to: `http://127.0.0.1:5000`

---

## 📂 Project Structure

```
├── app.py                 # Main Flask Application
├── utils.py               # Model Logic & Utility Functions
├── models/                # Pre-trained ML Models
├── templates/             # HTML Frontend Templates
│   ├── index.html         # Input Form
│   └── result.html        # Prediction Result with Gauges
├── data/                  # Datasets used for training
├── requirements.txt       # Project Dependencies
└── notebooks/             # Original Analysis & Training Notebooks (.ipynb)
```

---

## ⚖️ Disclaimer

This tool is a **prototype for educational and research purposes**. It is designed to demonstrate technical proficiency in Applied AI and ethical software design. It is **not** intended for real-world judicial decision-making without further rigorous validation and legal compliance checks.

---

**Author**: Yugal Jagtap