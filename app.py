import streamlit as st
from assistant.chat_interface import get_response
from assistant.financial_tips import suggest_tips
from models.default_predictor import predict_default

st.set_page_config(page_title="Debt Assistant", layout="centered")
st.title("💰 Personal Debt Management Assistant")

st.markdown("""
Ask me anything about your finances, debt, or budgeting!
""")

user_input = st.text_input("What would you like help with?")
if user_input:
    response = get_response(user_input)
    st.success(response)

st.subheader("📊 Predict Default Risk")
total_debt = st.number_input("Total Debt ($)", 0, 100000, 5000)
income = st.number_input("Monthly Income ($)", 0, 50000, 3000)
age = st.number_input("Age", 18, 100, 30)
payment_score = st.slider("Payment History Score (0-100)", 0, 100, 70)

if st.button("Predict Risk"):
    result = predict_default({
        'total_debt': total_debt,
        'income': income,
        'age': age,
        'payment_history_score': payment_score
    })
    st.info(f"Default Risk Level: **{result}**")

st.subheader("💡 Get Personalized Financial Tips")
entertainment = st.slider("Entertainment Spending ($)", 0, 2000, 400)
savings = st.slider("Savings ($)", 0, 5000, 250)
food = st.slider("Food Spending ($)", 0, 2000, 800)

if st.button("Suggest Tips"):
    tips = suggest_tips({
        'income': income,
        'entertainment': entertainment,
        'savings': savings,
        'food': food
    })
    for tip in tips:
        st.write("✅", tip)

