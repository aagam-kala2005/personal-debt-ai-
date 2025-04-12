import openai
openai.api_key = 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

def get_response(user_input, context=None):
    prompt = f"""
    You are a helpful financial advisor assistant. Your job is to help users manage their debt,
    suggest budgeting improvements, predict risk if needed, and explain refinancing options if asked.

    User: {user_input}
    Assistant:
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250,
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"I'm sorry, I couldn't process that. Error: {e}"

