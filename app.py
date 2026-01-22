import gradio as gr
import pandas as pd
import numpy as np
import pickle


indexes = [
    "Age",
    "Glucose",
    "BloodPressure",
    "Insulin",
    "BMI",
    "Pregnancies",
    "SkinThickness",
    "DiabetesPedigreeFunction",
]
# Load the model
with open("diabetes_classification.pkl", "rb") as file:
    model = pickle.load(file)


# Logic the function
def function_lg(
    Age,
    Glucose,
    BloodPressure,
    Insulin,
    BMI,
    Pregnancies,
    SkinThickness,
    DiabetesPedigreeFunction,
):
    input_df = pd.DataFrame(
        [
            [
                Age,
                Glucose,
                BloodPressure,
                Insulin,
                BMI,
                Pregnancies,
                SkinThickness,
                DiabetesPedigreeFunction,
            ]
        ],
        columns=[
            "Age",
            "Glucose",
            "BloodPressure",
            "Insulin",
            "BMI",
            "Pregnancies",
            "SkinThickness",
            "DiabetesPedigreeFunction",
        ],
    )
    predict = model.predict(input_df)[0]
    if predict:
        return f"Diabetes"
    else:
        return f"Not Diabetes"


# app interface
inputs = [
    gr.Number(label="Age", value=18),
    gr.Number(label="Glucose", value=150),
    gr.Number(label="BloodPessure", value=80),
    gr.Number(label="Insulin", value=50),
    gr.Number(label="BMI", value=35),
    gr.Slider(0, 7, step=1, label="Pregnancies"),
    gr.Number(label="SkinThickness", value=25),
    gr.Number(label="DiabetesPedigreeFunction", placeholder="0-3"),
]
# app launch
app = gr.Interface(
    fn=function_lg, inputs=inputs, outputs="text", title="Diabetes Prediction"
)
app.launch()
