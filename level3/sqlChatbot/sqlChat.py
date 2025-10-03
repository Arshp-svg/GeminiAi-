import os
import streamlit as st
import google.generativeai as genai
import sqlite3
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


#loading model
model=genai.GenerativeModel("gemini-2.0-flash-lite")

def get_response(question,prompt):
    try:
        response=model.generate_content([question,prompt])
        # Clean the response to remove unwanted formatting
        clean_sql = response.text.strip()
        # Remove markdown formatting
        clean_sql = clean_sql.replace('```sql', '').replace('```', '')
        # Remove common unwanted words/phrases
        clean_sql = clean_sql.replace('sql', '').replace('SQL', '')
        clean_sql = clean_sql.replace('undefined', '')
        # Remove extra whitespace and newlines
        clean_sql = ' '.join(clean_sql.split())
        return clean_sql.strip()
    except Exception as e:
        return f"Error: {str(e)}" 
    
    
#retrieving data from database
def retrieve_data(sql,db):
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        return f"Database error: {str(e)}"
    finally:
        if conn:
            conn.close()
            

prompt= """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - ID, NAME, CLASS, 
    SECTION, MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    \nExample 3 - Show students with marks above 90?, 
    the SQL command will be something like this SELECT NAME, MARKS FROM STUDENT 
    where MARKS > 90;
    \nExample 4 - What is the average marks of all students?, 
    the SQL command will be something like this SELECT AVG(MARKS) FROM STUDENT;
    
    IMPORTANT INSTRUCTIONS:
    - Return ONLY the SQL query, nothing else
    - Do NOT include ``` or ```sql in your response
    - Do NOT include the word 'sql' in your response
    - Do NOT include any explanations or additional text
    - Return a clean, executable SQL query only

    """

st.set_page_config(page_title="SQL Chatbot", page_icon=":robot_face:")
st.header("SQL Chatbot Usng Gemini Ai")

question=st.text_input("Ask your question related to SQL database :")
if st.button("Get Response"):
    response=get_response(question,prompt)
    st.write("SQL Query: ",response)
    data=retrieve_data(response,'test.db')
    for row in data:
        st.subheader(row)