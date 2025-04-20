from gemini_agent import generate_text

def search_jobs(role, location):
    prompt = f"Find top job roles for {role} in {location} on LinkedIn."
    return generate_text(prompt)