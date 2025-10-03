import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
from PIL import Image
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def find_nutrients(prompt, image):
    model=genai.GenerativeModel("gemini-2.0-flash-lite")
    response=model.generate_content([prompt, image[0]])
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
    
    
    
st.title("Nutrient Finder 🥦🍎")
uploaded_file=st.file_uploader("Upload an image of food", type=["png", "jpg", "jpeg"], key="file_uploader")
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit=st.button("Find Nutrients")
# ...existing code...

input_prompt = """
You are a friendly nutritionist. Look at the food in the image and tell me about its nutrition in simple terms.

Please provide:

FOOD IDENTIFICATION:
- What food is this?
- How much is in the image? (serving size)

NUTRITION FACTS:
- Calories
- Protein (grams)
- Carbohydrates (grams) 
- Fat (grams)
- Fiber (grams)
- Sugar (grams)
- Sodium (mg)
- Vitamin C
- Vitamin A
- Iron
- Calcium

SIMPLE SUMMARY:
- Is this food healthy?
- What's good about it?
- Anything to watch out for?

KEEP IT SIMPLE:
- Use easy-to-understand language
- Give approximate numbers
- If you can't see the food clearly, just say so
- If it's not food, politely say you can only analyze food items

Be accurate and concise in your response."""



if submit:
    img_data=input_image_details(uploaded_file)
    response=find_nutrients(input_prompt,img_data)
    st.subheader("Nutritional Information:")
    st.write(response)