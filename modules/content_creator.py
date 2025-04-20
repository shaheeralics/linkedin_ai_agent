from modules.gemini_agent import generate_text

def suggest_post(topic, tone, goal):
    prompt = f'''
You're a LinkedIn influencer coach.

Write a LinkedIn post on the topic: {topic}
Tone: {tone}
Goal: {goal}

The post should:
- Be engaging from the first line
- Include personal insights
- Use hashtags
- End with a question to encourage comments

Make it sound human and real.
'''
    return generate_text(prompt)