import base64
import streamlit as st
import io
import pdf2image
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


genai.configure(api_key=GOOGLE_API_KEY)

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,pdf_content[0],prompt])
    print(response.text)
    try:
    # Check if 'candidates' list is not empty
        if response.candidates:
            # Access the first candidate's content if available
            if response.candidates[0].content.parts:
                generated_text = response.candidates[0].content.parts[0].text
                return generated_text
            else:
                return "No generated text found in the candidate."
        else:
            return "No candidates found in the response."
    except (AttributeError, IndexError) as e:
        print("Error:", e)

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

## Streamlit App

st.set_page_config(page_title="ATS Catalyst - Streamlining Resume Screening with AI")
st.header("ATS Catalyst - AI-Powered Resume Feedback System")
input_text = st.text_area("Job Description: ",key="input")
uploaded_file = st.file_uploader("Upload your resume(Format should be in PDF)",type=["pdf"])


if uploaded_file is not None:
    st.write('Resume Uploaded Successfully')
else:
    st.write('Please Upload Your Resume In PDF Format.')


get_feedback_submit_btn = st.button("Get The Feedback From AI HR Manager")

feedback_prompt = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

if get_feedback_submit_btn:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(prompt=feedback_prompt,pdf_content=pdf_content,input=input_text)
        st.write(response)
    else:
        st.write("Please uplaod the resume")