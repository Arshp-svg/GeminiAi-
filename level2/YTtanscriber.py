import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from youtube_transcript_api import YouTubeTranscriptApi


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

prompt="""
You are an expert note-taker and content summarizer. Analyze the YouTube video transcript and create detailed, structured notes in a concise format.

STRUCTURE YOUR NOTES AS FOLLOWS:

📋 **OVERVIEW**
- Brief 2-3 sentence summary of the video's main topic and purpose

🎯 **KEY POINTS**
- List 5-7 main points discussed (use bullet points)
- Include important facts, statistics, or examples mentioned

💡 **MAIN IDEAS & CONCEPTS**
- Core concepts explained in the video
- Important terminology or definitions
- Key insights or takeaways

🔍 **DETAILS & EXAMPLES**
- Specific examples, case studies, or demonstrations
- Step-by-step processes if mentioned
- Important quotes or statements

📌 **ACTION ITEMS/RECOMMENDATIONS**
- Any advice, tips, or recommendations given
- Practical steps viewers should take

⚡ **QUICK SUMMARY**
- 1-2 sentence conclusion summarizing the video's value

FORMATTING REQUIREMENTS:
- Use clear, concise bullet points
- Keep each point under 2 lines
- Focus on actionable and memorable information
- Remove filler words and redundant content
- Maintain logical flow and organization

The transcript is appended here:
"""
def extract_transcript_details(youtube_video_url):
    try:
        # Extract video ID more robustly
        if "v=" in youtube_video_url:
            video_id = youtube_video_url.split("v=")[1].split("&")[0]
        else:
            video_id = youtube_video_url.split("=")[1]
        
        # Create an instance of the API and get transcript
        api = YouTubeTranscriptApi()
        transcript_text = api.fetch(video_id=video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i.text

        return transcript

    except Exception as e:
        return f"Error fetching transcript: {str(e)}. Video may not have captions or may be restricted."
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,prompt):
    try:
        model=genai.GenerativeModel("gemini-2.0-flash-lite")
        response=model.generate_content(prompt+transcript_text)
        return response.text
    except Exception as e:
        return f"Error generating summary: {str(e)}"

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    vid_id = youtube_link.split("=")[1]
    print(vid_id)
    st.image(f"http://img.youtube.com/vi/{vid_id}/0.jpg", use_container_width=True)

if st.button("Get Detailed Notes", key="get_notes_btn"):
    if youtube_link:
        with st.spinner("Fetching transcript..."):
            transcript_text = extract_transcript_details(youtube_link)

        if transcript_text and not transcript_text.startswith("Error"):
            with st.spinner("Generating summary..."):
                summary = generate_gemini_content(transcript_text, prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)
        else:
            st.error(transcript_text if transcript_text.startswith("Error") else "Failed to get transcript")
    else:
        st.warning("Please enter a YouTube video link first")

