from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import os
import google.generativeai as genai


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model=genai.GenerativeModel("gemini-2.0-flash-lite")

def get_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text


def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts

    else:
        raise FileNotFoundError("No file uploaded")



st.title("MultiLanguage Invoice Chatbot 🤖")

input=st.text_input("Enter your query: ", key="input")
uploaded_file=st.file_uploader("Upload an invoice image", type=["png", "jpg", "jpeg"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit=st.button("Get Response")
input_prompt="""

You are an AI assistant that helps people find information about their invoices.
You will be provided with an image of an invoice and a question about the invoice.
Please answer the question based on the information in the invoice.
If the question is not related to the invoice, politely inform them that you are only able to answer questions related to the invoice."""



if submit:
    img_data=input_image_details(uploaded_file)
    response=get_response(input_prompt,img_data,input)
    st.subheader("Response:")
    st.write(response)