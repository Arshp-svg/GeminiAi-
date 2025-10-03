#qna chatbot with memory
from dotenv import load_dotenv
import google.generativeai as genai
import os
import streamlit as st

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model=genai.GenerativeModel("gemini-2.0-flash-lite")
chat=model.start_chat(history=[])

def get_response(prompt):
    try:
        response = chat.send_message(prompt, stream=True)
        return response
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

st.set_page_config(page_title="QnA Chatbot with Memory", page_icon="🤖")
st.title("QnA Chatbot with Memory 🤖")


# Initialize chat history in session state
if 'Chat_History' not in st.session_state:
    st.session_state['Chat_History'] = []

prompt=st.text_input("You: ", key="prompt")
submit_button=st.button("Get Response")

if submit_button and prompt:
    response = get_response(prompt)
    if response:  # Only proceed if response is not None
        st.session_state['Chat_History'].append(("You", prompt))
        st.subheader("Response:")
        
        # Collect all chunks into a single response
        full_response = ""
        response_placeholder = st.empty()
        
        for chunk in response:
            full_response += chunk.text
            response_placeholder.write(full_response)
        
        # Add the complete response to chat history
        st.session_state['Chat_History'].append(("Bot", full_response))
        
st.subheader("Chat History:")
for sender, message in st.session_state['Chat_History']:
    st.write(f"**{sender}:** {message}")