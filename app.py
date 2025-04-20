import streamlit as st
from gemini_agent import generate_text
from job_search import search_jobs
from profile_optimizer import optimize_profile
from lead_generation import generate_leads
from content_creator import suggest_post
from message_sender import send_message

st.title("🔗 LinkedIn AI Agent")

task = st.sidebar.selectbox("Choose a Task", [
    "Profile Optimizer", "Job Search Assistant", 
    "Lead Generation", "Content Creator", "Messaging Assistant"
])

if task == "Profile Optimizer":
    profile_text = st.text_area("Paste your LinkedIn Summary")
    if st.button("Optimize"):
        st.write(optimize_profile(profile_text))

elif task == "Job Search Assistant":
    role = st.text_input("Role")
    location = st.text_input("Location")
    if st.button("Search Jobs"):
        st.write(search_jobs(role, location))

elif task == "Lead Generation":
    industry = st.text_input("Industry")
    if st.button("Generate Leads"):
        st.write(generate_leads(industry))

elif task == "Content Creator":
    topic = st.text_input("Topic")
    if st.button("Suggest Post"):
        st.write(suggest_post(topic))

elif task == "Messaging Assistant":
    context = st.text_area("Enter context for the message")
    if st.button("Generate Message"):
        st.write(send_message(context))