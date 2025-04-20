from modules.gemini_agent import generate_text

def search_jobs(role, location, filters=""):
    prompt = f'''
Act like a professional LinkedIn job search assistant.
Give me top job listings or types of roles for the following:

Role: {role}
Location: {location}
Filters: {filters}

Give a short, easy-to-read list with suggestions and why each is a good fit.
'''
    return generate_text(prompt)