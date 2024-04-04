import streamlit as st
import json
from streamlit_lottie import st_lottie


st.set_page_config(page_title="ATS Catalyst - AI-Powered Recruitment Suite", layout="wide", page_icon=':tada:')

def load_lottiefile(filepath):
    with open(filepath, "r") as f:
        return json.load(f)


def load_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("style/style.css")

lottie_hello = load_lottiefile("assets/hello.json")
lottie_features = load_lottiefile("assets/features.json")

lottie_how_its_works = load_lottiefile("assets/how_works.json")

lottie_open_source = load_lottiefile("assets/open_source.json")


with st.container():
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.header("Welcome to ATS Catalyst - Your AI Powered Recruitment Suite")
        st.markdown('''ATS Catalyst is an innovative platform designed to empower job seekers and streamline the hiring process. Leveraging advanced AI technologies, our suite of tools offers personalized feedback, resume evaluation, and job description matching to enhance your job application process.
                    ''')
    
    with right_column:
        st_lottie(lottie_hello, key="hello", height=300, width=400)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Features Overview 🚀")
        st.markdown("""
        **Key Features of ATS Catalyst:**
        - **Resume Evaluator:** Get instant feedback on your resume with detailed scores and suggestions for improvement.
        - **Project Generator:** Generate project ideas based on job descriptions to enhance your resume.
        - **Match Analyzer:** Find out how well your resume matches a job description.
        - **AI HR Manager Feedback:** Receive professional feedback from an AI-powered HR manager.
        """)
    
    with right_column:
        st_lottie(lottie_features, width=400, height=300)



with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How It Works 🔍")
        st.markdown("""
        **Getting Started with ATS Catalyst is Easy:**
        1. **Choose a Service:** Select from our range of services - Resume Evaluation, Project Generation, Match Analysis, or AI HR Manager Feedback.
        2. **Upload Your Resume:** Start by uploading your resume in PDF format.
        3. **Receive Insights:** Get detailed feedback and insights to improve your job application process.
        """)
    
    with right_column:
        st_lottie(lottie_how_its_works, width=400, height=300)



with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Open Source & Collaboration🌍👥")
        st.markdown("""
        This project is proudly open-source, and we welcome contributors who share our vision of revolutionizing the job application process. Whether you're a developer, a designer, or an HR professional, there's a way for you to contribute.
        - **GitHub Repository**: [Link to GitHub](https://github.com)
        - **Contribution Guidelines**: [Find out how you can contribute to our project.](https://github.com/CONTRIBUTING.md)
        - **Community**: [Join our community](https://community.link) to discuss features, share ideas, and collaborate.
        """)
    
    with right_column:
        st_lottie(lottie_open_source, width=400, height=300)
