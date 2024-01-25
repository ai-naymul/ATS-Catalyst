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

st.header('Resume Evaluator By ATS Catalyst')
st.subheader("Resume Evaluator")
experience_weight = st.slider("Experience Weight", 0, 10, 5)
skills_weight = st.slider("Skills Weight", 0, 10, 5)
education_weight = st.slider("Education Weight", 0, 10, 5)
keywords_weight = st.slider("Keywords Weight", 0, 10, 5)




