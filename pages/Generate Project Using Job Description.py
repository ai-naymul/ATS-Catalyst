import streamlit as st
from google.generativeai import GenerativeModel
from main import get_gemini_response, input_pdf_setup
import google.generativeai as genai


GOOGLE_API_KEY = "AIzaSyD3ppjOkpyQCxuZmEFKy-V3mTAhaAnypnw"

genai.configure(api_key=GOOGLE_API_KEY)



# Configure the stramlit application
st.set_page_config(page_title='Generate Projects Using the Job Description and Resume')
st.header('Resume-Driven Project Recommender')
st.markdown("""Instructions: 
            \n 1. Copy the job description.
            \n 2. Paste it into the job description input section.
            \n 3. Upload the resume.
            \n 4. Press the relevent button to get the result.
            \n That's how it so simple to use😉.""")
## Get input the job description

job_description = st.text_area("Enter the job description...", key="input")

prompt = f"""I want you to respond only in English(US). 
Act in the role of a specialist in analyzing job description ad generating projects that companies will like. 
The writing style should be to-the -point abd straightford. 
Lease provide project recommendation that align with a company's interest and job description, 
along with the technologies I should use for the projects to maximize my chances to getting shortlisted. 
Present the information in a columns and rows containing the project title, 
project description, 
technologies to be used, 
a basic brief on how to get it done, 
and a column ranking the projects by percentage chance of getting shortlisted. 
Here is the job description to consider.{job_description}"""

upload_resume = st.file_uploader('Upload your resume...',type=['pdf'])



generate_projects = st.button('Generate Project')


if generate_projects:
    if upload_resume is not None:
        st.write('Resume Uploaded Successfully')
        # use the method from the main
        resume_content= input_pdf_setup(uploaded_file=upload_resume)
        response = get_gemini_response(prompt=prompt,pdf_content=resume_content,input=job_description)
        st.write("Here are some projects matching with the job description")
        st.write(response)
    else:
        st.write('Please Upload Your Resume In PDF Format.')


