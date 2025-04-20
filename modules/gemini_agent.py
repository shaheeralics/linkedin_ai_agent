import streamlit as st
import google.generativeai as genai

# Configure Gemini with Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_text(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text.strip()