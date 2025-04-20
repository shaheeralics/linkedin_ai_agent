import streamlit as st
from modules.gemini_agent import generate_text
from modules.job_search import search_jobs
from modules.profile_optimizer import optimize_profile
from modules.lead_generation import generate_leads
from modules.content_creator import suggest_post
from modules.message_sender import send_message

st.set_page_config(page_title="LinkedIn Agent Pro", page_icon="🔗", layout="centered")

st.title("🔗 LinkedIn Agent Pro – AI-Powered LinkedIn Assistant")

st.sidebar.header("Choose a Smart Assistant Tool")
task = st.sidebar.radio("What do you want help with?", [
    "Profile Optimizer", 
    "Job Search Assistant", 
    "Lead Generation", 
    "Content Creator", 
    "Messaging Assistant"
])

if task == "Profile Optimizer":
    st.subheader("📌 Paste your LinkedIn Summary below:")
    profile_text = st.text_area("Your current summary", height=200)
    if st.button("🚀 Improve My Profile"):
        st.write(optimize_profile(profile_text))

elif task == "Job Search Assistant":
    st.subheader("🔍 Enter job search details:")
    role = st.text_input("Job Title or Role")
    location = st.text_input("Preferred Location")
    filters = st.text_area("Add any filters (remote, salary, experience, etc.)")
    if st.button("🧠 Find Jobs"):
        st.write(search_jobs(role, location, filters))

elif task == "Lead Generation":
    st.subheader("🎯 Generate potential leads")
    industry = st.text_input("Target Industry")
    position = st.text_input("Target Position (e.g., Marketing Manager)")
    if st.button("📇 Generate Leads"):
        st.write(generate_leads(industry, position))

elif task == "Content Creator":
    st.subheader("✍️ Need help writing a post?")
    topic = st.text_input("Topic for LinkedIn Post")
    tone = st.selectbox("Tone", ["Professional", "Casual", "Inspirational", "Witty"])
    goal = st.text_area("Goal (e.g., engagement, awareness, lead gen)")
    if st.button("📝 Suggest Post"):
        st.write(suggest_post(topic, tone, goal))

elif task == "Messaging Assistant":
    st.subheader("📨 Personalized Messaging Assistant")
    context = st.text_area("Who are you messaging and why? (e.g., recruiter follow-up)")
    tone = st.selectbox("Message Tone", ["Polite", "Direct", "Enthusiastic", "Empathetic"])
    if st.button("✉️ Generate Message"):
        st.write(send_message(context, tone))