import joblib
import pandas as pd

model = joblib.load("models/default_predictor.pkl")

def predict_default(user_data):
    # user_data = {total_debt, income, age, payment_history_score}
    input_df = pd.DataFrame([user_data])
    prediction = model.predict(input_df)[0]
    return "High Risk" if prediction == 1 else "Low Risk"

