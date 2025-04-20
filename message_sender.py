from gemini_agent import generate_text

def send_message(context):
    prompt = f"Write a professional and personalized LinkedIn message based on this: {context}"
    return generate_text(prompt)