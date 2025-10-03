from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#loading model
model=genai.GenerativeModel("gemini-2.0-flash-lite")
def get_response(prompt):
    try:
        response=model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


st.set_page_config(page_title="Q & A Bot ", page_icon=":robot_face:")
st.header("Gemini LLM Application")

prompt=st.text_input("Ask me anything :")
if st.button("Get Response"):
    response=get_response(prompt)
    st.write(response)