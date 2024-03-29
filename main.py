from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyCDthI_42EJCNEKg5rwF9BfCVrh2GUmwVI"))

model = genai.GenerativeModel('gemini-pro')

# ... your existing imports ...

def get_gemini_response(question):
    if not is_about_human_characters(question):  # We'll define this function below
        return "Please ask a question about a human character or situation."

    # ... (Your code to generate a response with the model) ... 

def is_about_human_characters(question):
    keywords = ["person", "people", "human", "character", "relationship", "friend", "family",  # Expand this list
               "love", "emotion", "behavior"]
    return any(word in question.lower() for word in keywords)

# ... (Rest of your Streamlit code) ... 


def get_gemini_response(question):
    response = model.generate_content(question)
    text = response.text

    # Limit the response to 100 words
    words = text.split()
    limited_response = " ".join(words[:100]) 

    return limited_response  

st.set_page_config(page_title="Q&A Demo ")
st.header("Ask Gemini about Human Characters & Situations")
st.write("Examples: 'What makes a good leader?', 'How do people cope with loss?', 'Why do friends sometimes argue?', 'why do couples sometimes argue?'")

input = st.text_input("Input (limit 100 characters):", key="input", max_chars=100) 
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is ") 
    st.write(response)  


    









