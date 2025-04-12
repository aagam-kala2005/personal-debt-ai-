def suggest_tips(spending_data):
    tips = []
    income = spending_data.get('income', 1)

    if spending_data.get('entertainment', 0) > 0.2 * income:
        tips.append("Consider reducing entertainment expenses to under 20% of your income.")
    if spending_data.get('savings', 0) < 0.1 * income:
        tips.append("Aim to save at least 10% of your monthly income.")
    if spending_data.get('food', 0) > 0.4 * income:
        tips.append("Track food expenses—try meal prepping to save money.")
    return tips if tips else ["Your spending looks good! Keep it up."]

