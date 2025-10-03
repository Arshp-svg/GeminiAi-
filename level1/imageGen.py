from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#loading model
model=genai.GenerativeModel("gemini-2.0-flash-lite")
def get_response(prompt,image):
    if prompt!="":
        response=model.generate_content([prompt,image])
    else:
        response=model.generate_content(image)
    return response.text

st.title("Gemini Image to text Gen")
prompt=st.text_input("Ask me anything :")
uploaded_file=st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
image=""
if st.button("Get Response"):
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")
    response=get_response(prompt,image)
    st.write(response)