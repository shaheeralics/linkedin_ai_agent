from modules.gemini_agent import generate_text

def optimize_profile(profile_summary):
    prompt = f'''
You're an expert LinkedIn career coach.

Improve this profile summary by:
- Making it more engaging and human
- Using strong action verbs
- Keeping it professional but friendly
- Making it attractive to recruiters

Here is the original summary:
"""
{profile_summary}
"""

Give the improved version:
'''
    return generate_text(prompt)