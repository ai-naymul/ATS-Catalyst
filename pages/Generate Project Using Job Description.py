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


