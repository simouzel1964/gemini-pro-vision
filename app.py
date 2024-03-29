import streamlit as st
from langchain_google_genai.llms import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()  # Load environment variables for your API key

def generate_human_psychological_characters(psychological_characters):
    llm = GoogleGenerativeAI(model="gemini-pro", temperature=0.7)

    prompt_template = PromptTemplate(
        input_variables=['psychological_characters'],
        template="Please provide detailed information about {psychological_characters}, including its symptoms, causes, diagnosis process, treatment options, and self-care tips. Focus on providing a supportive and informative explanation."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template)
    response = name_chain({'psychological_characters': psychological_characters})
    return response

if __name__ == "__main__":
    st.title("Psychological Character Guide")

    selected_character = st.sidebar.selectbox(
        "What is your Character?", 
        ("Empathy", "Resilience", "Self-esteem", 
         "Self-awareness", "Emotional Intelligence", 
         "Introversion vs Extroversion", "Neuroticism", "Locus of Control", "Optimism", "Agreeableness")
    )

    if selected_character:  # Check if a character is selected
        result = generate_human_psychological_characters(selected_character)
        st.write(result)