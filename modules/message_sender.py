from modules.gemini_agent import generate_text

def send_message(context, tone):
    prompt = f'''
You're a LinkedIn messaging expert.

Write a personalized LinkedIn message based on this context:
"""
{context}
"""

Use a {tone} tone.

Keep it:
- Brief
- Professional
- Friendly
- Human-sounding

Output just the message content.
'''
    return generate_text(prompt)