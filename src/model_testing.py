import os

import joblib
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
ROOT = os.path.dirname(BASE_DIR)
MODELS_PATH = os.path.join(ROOT, 'models')

model = joblib.load(os.path.join(MODELS_PATH, 'svm_diabetes_prediction_model.pkl'))

labels = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction',
          'Age']
vals = []
outcome_map = {0: 'No Diabetes', 1: 'Diabetes'}


def make_prediction(features):
    df = pd.DataFrame([features], columns=labels)

    prediction = outcome_map[model.predict(df)[0]]
    return prediction


if __name__ == '__main__':
    for i in labels:
        val = input(f"{i}: ")
        vals.append(val)

    predict = make_prediction(vals)
    print(predict)
