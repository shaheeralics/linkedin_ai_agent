from gemini_agent import generate_text

def suggest_post(topic):
    prompt = f"Write a professional LinkedIn post about {topic} that encourages engagement."
    return generate_text(prompt)