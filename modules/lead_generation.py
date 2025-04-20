from modules.gemini_agent import generate_text

def generate_leads(industry, position):
    prompt = f'''
You're a LinkedIn growth strategist.

Suggest 5 potential leads (name-style placeholders) in the industry below:
Industry: {industry}
Position: {position}

For each lead, include:
- Full Name (realistic)
- Job Title
- Company
- City
- Why they’re a good lead

Keep the tone natural and helpful.
'''
    return generate_text(prompt)