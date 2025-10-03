#Multiple PDF chat With Gemini AI
import os
import streamlit as st
import google.generativeai as genai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS


load_dotenv()

# Check if API key is available
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("❌ API Key not found! Please set GOOGLE_API_KEY or GEMINI_API_KEY in your .env file")
    st.stop()

# Set your Google Generative AI API key
genai.configure(api_key=api_key)

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text 

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000,
        chunk_overlap=1000,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    # Use HuggingFace embeddings (free and no quota limits)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_convo_chain():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-lite", 
        temperature=0.3,
        google_api_key=api_key
    )
    prompt_template = """Use the following pieces of context to answer the question at the end. 
    If you don't know the answer, just say that you don't know, don't try to make up an answer. 
    Context:\n{context}?\n
    Question: \n {question}\n
    Answer:
    """
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=PROMPT)
    return chain


def user_input(query):
    # Use HuggingFace embeddings (free and no quota limits)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    new_db=FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    doxs=new_db.similarity_search(query)
    chain = get_convo_chain()

    response=chain({"input_documents": doxs, "question": query}, return_only_outputs=True)
    st.write( "Reply: ",response['output_text'])
    
    

def main():
    st.set_page_config(page_title="PDF Chat", page_icon="�")
    st.title("Multi PDF Chat with Gemini AI")
    
    # File upload
    pdf_docs = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
    
    # Process button
    if st.button("Process PDFs"):
        if pdf_docs:
            with st.spinner("Processing..."):
                try:
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    vectorstore = get_vectorstore(text_chunks)
                    vectorstore.save_local("faiss_index")
                    st.success("PDFs processed successfully!")
                    st.session_state.processed = True
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please upload PDF files first")
    
    # Chat section
    if 'processed' in st.session_state:
        st.subheader("Ask a question about your PDFs:")
        user_question = st.text_input("Your question:")
        
        if st.button("Get Answer"):
            if user_question:
                try:
                    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
                    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
                    docs = new_db.similarity_search(user_question)
                    chain = get_convo_chain()
                    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
                    st.write("**Answer:**", response['output_text'])
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter a question")
    else:
        st.info("Please upload and process PDF files first")

if __name__ == "__main__":
    main()
    