import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai


GOOGLE_API_KEY = "AIzaSyD3ppjOkpyQCxuZmEFKy-V3mTAhaAnypnw"

genai.configure(api_key=GOOGLE_API_KEY)


## Get The response from gemini pro using that api

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text


## handle the pdf stuff

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


## Streamlit app configuration

st.set_page_config(page_title="Resume Evaluator By ATS Catalyst")
st.header('Resume Evaluator')
st.subheader("Resume Evaluator")
st.markdown('''The Scoring Is 1-100 
            Ranges: 
            \n **Excellent (81-100)🥇**
            \n **Good (61-80) 👍**
            \n **Average (41-60) 🤔**
            \n **Below Average (21-40) 😐**
            \n **Poor (1-20) 😑👎**
            ''')

upload_resume = st.file_uploader('Upload Your Resume(PDF)....', type=['pdf'])


if upload_resume is not None:
    st.write('Resume Uploaded Successfully')
else:
    st.write('Please Upload Your Resume In PDF Format.')

submit = st.button('Get The Score')


input_prompt = '''You are a great resume evaluator with deep understaning of ATS(Application Tracking Systems) and ATS functionality,
your task is to evaluate the resume according to a score The scoring range is [Excellent (81-100) , Good (61-80), 
Average (41-60), Below Average (21-40), Poor (1-20)]. So give a score to the regarding resume the range I give to you
and evaluate the score and the resume and evaluate the resume according to the education, skills, projects, resume structure, resume readability,
experience, contributions, volunter works, certification, grades, how Tailored Content are, Professional Summary, Quantifiable Achievements,
Relevant Skills, Clear Formatting, Correct Spelling and Grammar, Strong Action Verbs and so on '''

input = "There will be three section one is for Score,one for what the things are good in the resume, one is for What the things to change, one for what the things to add, one for what the things to exclude, one for how to make it more impactful and enagnign to recruiters"

if submit:
    pdf_content = input_pdf_setup(upload_resume)
    response= get_gemini_response(input,pdf_content,input_prompt)
    st.subheader("The Score and Feedback Is:")
    st.write(response)

