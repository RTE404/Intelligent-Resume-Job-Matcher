import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/match"

st.set_page_config(page_title="Resume Job Matcher", layout="centered")

st.title("Intelligent Resume–Job Matcher")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if st.button("Match"):
    if resume_file is None or not job_description:
        st.error("Please upload resume and enter job description.")
    else:
        files = {
            "resume": resume_file
        }

        data = {
            "job_description": job_description
        }

        with st.spinner("Analyzing..."):
            response = requests.post(API_URL, files=files, data=data)

        if response.status_code == 200:
            result = response.json()["result"]
            st.subheader("Result")
            st.write(result)
        else:
            st.error("Error from backend.")
