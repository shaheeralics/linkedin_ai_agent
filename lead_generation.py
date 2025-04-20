from gemini_agent import generate_text

def generate_leads(industry):
    prompt = f"Give me a list of 5 LinkedIn leads in the {industry} industry with names and sample titles."
    return generate_text(prompt)