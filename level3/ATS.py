import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
import re
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def get_response(prompt, resume_text):
    model = genai.GenerativeModel("gemini-2.0-flash-lite")
    full_prompt = f"{prompt}\n\nResume Text:\n{resume_text}"
    response = model.generate_content(full_prompt)
    return response.text


def extract_text_from_pdf(pdf_file):
    if pdf_file is not None:
        try:
            pdf_reader = PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            
            if not text.strip():
                return "No text could be extracted from the PDF."
            return text
        except Exception as e:
            raise Exception(f"Error reading PDF: {str(e)}")
    else:
        raise FileNotFoundError("No PDF file uploaded.")


def get_response(prompt, resume_text):
    """Get AI response from Gemini"""
    try:
        # Configure Gemini
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model = genai.GenerativeModel('gemini-2.0-flash-lite')
        
        # Combine prompt and resume text
        full_prompt = f"{prompt}\n\nResume Text:\n{resume_text}"
        
        # Get response
        response = model.generate_content(full_prompt)
        return response.text
        
    except Exception as e:
        return f"Error generating response: {str(e)}"


def calculate_match_score(resume_text, job_description):
    """Simple keyword matching for ATS score"""
    # Common important keywords
    tech_keywords = ['python', 'java', 'javascript', 'sql', 'aws', 'azure', 'react', 'node.js', 
                    'machine learning', 'data science', 'git', 'docker', 'kubernetes']
    soft_keywords = ['leadership', 'communication', 'teamwork', 'problem solving', 'project management']
    
    resume_lower = resume_text.lower()
    job_lower = job_description.lower()
    
    # Find keywords in job description
    job_keywords = [kw for kw in tech_keywords + soft_keywords if kw in job_lower]
    
    # Find matching keywords in resume
    matching_keywords = [kw for kw in job_keywords if kw in resume_lower]
    
    # Calculate percentage
    if not job_keywords:
        return 50, matching_keywords, []
    
    score = (len(matching_keywords) / len(job_keywords)) * 100
    missing_keywords = [kw for kw in job_keywords if kw not in matching_keywords]
    
    return score, matching_keywords, missing_keywords


def extract_text_from_pdf(pdf_file):
    if pdf_file is not None:
        try:
            # Use PyPDF2 to extract text from PDF
            pdf_reader = PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            
            if not text.strip():
                return "No text could be extracted from the PDF. Please ensure the PDF contains readable text."
            
            return text
        except Exception as e:
            raise Exception(f"Error reading PDF: {str(e)}")
    else:
        raise FileNotFoundError("No PDF file uploaded.")
    
    
    
# Simple Streamlit App
st.set_page_config(page_title="Simple ATS Resume Screener", page_icon="📄")

st.title("📄 Simple ATS Resume Screener")
st.markdown("Upload your resume and job description for AI-powered analysis")

# Input sections
st.subheader("Job Description")
job_description = st.text_area("Enter the job description:", height=150, 
                              placeholder="Paste the complete job description here...")

st.subheader("Resume Upload")
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success(f"✅ {uploaded_file.name} uploaded successfully")

# Analysis buttons
col1, col2, col3 = st.columns(3)
with col1:
    analyze_btn = st.button("� Analyze Resume", use_container_width=True)
with col2:
    score_btn = st.button("🎯 Get ATS Score", use_container_width=True) 
with col3:
    improve_btn = st.button("💡 Suggestions", use_container_width=True)

# Simple prompts
analyze_prompt = """
You are an HR specialist. Analyze this resume and provide:
1. Brief summary of candidate's background
2. Key skills and strengths 
3. Experience level
4. Overall assessment

Job Description: {job_desc}
"""

score_prompt = """
You are an ATS system. Compare this resume with the job requirements and provide:
1. Match score (0-100%)
2. Matching skills found
3. Missing important skills
4. Recommendation (Hire/Consider/Reject)

Job Description: {job_desc}
"""

suggestions_prompt = """
You are a career advisor. Based on the job requirements, suggest improvements for this resume:
1. Skills to highlight or add
2. Keywords to include
3. Experience to emphasize
4. Overall formatting tips

Job Description: {job_desc}
"""

# Analysis functions
if analyze_btn:
    if uploaded_file and job_description:
        try:
            with st.spinner("Analyzing resume..."):
                resume_text = extract_text_from_pdf(uploaded_file)
                prompt = analyze_prompt.format(job_desc=job_description)
                response = get_response(prompt, resume_text)
                
                st.subheader("� Resume Analysis")
                st.write(response)
                
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please upload a resume and enter job description.")

if score_btn:
    if uploaded_file and job_description:
        try:
            with st.spinner("Calculating ATS score..."):
                resume_text = extract_text_from_pdf(uploaded_file)
                
                # Simple keyword matching
                score, matching, missing = calculate_match_score(resume_text, job_description)
                
                # Display score
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("🎯 ATS Score", f"{score:.0f}%")
                with col_b:
                    status = "PASS" if score >= 60 else "NEEDS WORK"
                    st.metric("📋 Status", status)
                
                # AI analysis
                prompt = score_prompt.format(job_desc=job_description)
                response = get_response(prompt, resume_text)
                
                st.subheader("🎯 Detailed ATS Score")
                st.write(response)
                
                if matching:
                    st.subheader("✅ Matching Keywords")
                    st.success(" • ".join(matching))
                
                if missing:
                    st.subheader("❌ Missing Keywords")
                    st.error(" • ".join(missing[:5]))  # Show top 5
                
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please upload a resume and enter job description.")

if improve_btn:
    if uploaded_file and job_description:
        try:
            with st.spinner("Generating suggestions..."):
                resume_text = extract_text_from_pdf(uploaded_file)
                prompt = suggestions_prompt.format(job_desc=job_description)
                response = get_response(prompt, resume_text)
                
                st.subheader("💡 Improvement Suggestions")
                st.write(response)
                
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please upload a resume and enter job description.")

# Simple footer
st.markdown("---")
st.markdown("**Simple ATS Resume Screener** - Powered by Gemini AI 🤖")