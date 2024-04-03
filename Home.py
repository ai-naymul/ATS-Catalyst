import streamlit as st
import json
from streamlit_lottie import st_lottie


st.set_page_config(page_title="ATS Catalyst - AI-Powered Recruitment Suite")

def load_lottiefile(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_hello = load_lottiefile("assets/hello.json")

with st.container():
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.header("Welcome to ATS Catalyst - Your AI Powered Recruitment Suite")
        st.markdown('''ATS Catalyst is an innovative platform designed to empower job seekers and streamline the hiring process. Leveraging advanced AI technologies, our suite of tools offers personalized feedback, resume evaluation, and job description matching to enhance your job application process.
                    ''')
    
    with right_column:
        st_lottie(lottie_hello, key="hello", height=300, width=400)

