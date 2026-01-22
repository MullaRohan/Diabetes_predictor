# ✒️ About Project 
# ✍️ Diabetes Prediction Project

## 🗒️Project Overview
This project focuses on **classification task** for predicting diabetes using the **Pima Indians Diabetes Dataset**. The goal is to accurately identify individuals who are likely to have diabetes, aiding early diagnosis and preventive healthcare.

---

## 🗒️Dataset
- Source: Pima Indians Diabetes Dataset
- Features: Numeric and categorical features including:
  - Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
- Target: `Outcome` (0 = non-diabetic, 1 = diabetic)
- Total samples: ~768
- Imbalance: Fewer positive cases (~268) than negative (~500)

---

## 🗒️Data Preprocessing
- Missing and zero values handled with **median imputation**.
- Outliers in numeric features were clipped (1%–99% quantiles).
- Numeric features scaled using **StandardScaler**.
- Categorical features encoded using **OneHotEncoder**.
- Pipelines used to integrate preprocessing and ensure reproducibility.

---

## 🗒️Model Selection
- **Primary model**: Logistic Regression
- Alternative models evaluated: SVC, KNN
- **Evaluation metric**: Recall for positive class (Outcome=1) prioritized due to medical significance.

---

## 🗒️Model Training and Evaluation
- Pipeline created using **ColumnTransformer** and preprocessing.
- Models trained on stratified train-test split to handle class imbalance.
- **Cross-validation (5-fold)** applied to assess model robustness.
- Metrics recorded: Accuracy, Precision, Recall, F1-score (positive class).

---

## 🗒️Key Findings
- Logistic Regression with **class_weight="balanced"** achieved highest recall for diabetic cases.
- KNN showed higher F1 but lower recall.
- Weighted metrics can be misleading due to dataset imbalance; **positive class recall is primary metric**.

---

## 🗒️Deployment
- Final pipeline saved as `.pkl` file.
- Front-end can pass input as dictionary or DataFrame.
- Column order flexibility maintained; column names must match pipeline requirements.

---

## 🗒️Technologies & Libraries
- Python 3.x
- Pandas, NumPy
- scikit-learn
- Matplotlib / Seaborn (EDA & visualization)
- Joblib / Pickle (pipeline serialization)

---


# ✍️Project Setup & Run Instructions

This guide explains how to set up the Python environment and run the project.

---

## 1. Create Python Environment

Create a new virtual environment for this project:

```bash
python -m venv aiml_env
```

## 2. Activate Environment

Activate the newly created environment:
```bash
aiml_env\Scripts\activate
```

## 3. Install Dependencies
Install all required packages from ***requirements.txt***:
```bash
pip install -r requirements.txt
```

## 4. Run the application
Start projet by typing: 
```bash
python app.py
```
---
## 🗒️References
- [Pima Indians Diabetes Dataset – Kaggle](https://www.kaggle.com/uciml/pima-indians-diabetes-database)
- scikit-learn documentation: [Pipeline & ColumnTransformer](https://scikit-learn.org/stable/modules/compose.html)

---
If you faced any kind of issue feel free to Report:  
Name: MD Rohan Mulla
🎓University: Rabindra Maitree University
📨E-mail: mdrohanislam444@gmail.com
facebook: https://www.facebook.com/MullaRohan