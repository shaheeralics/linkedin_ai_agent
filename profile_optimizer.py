from gemini_agent import generate_text

def optimize_profile(profile_summary):
    prompt = f"Improve this LinkedIn profile summary: {profile_summary}"
    return generate_text(prompt)