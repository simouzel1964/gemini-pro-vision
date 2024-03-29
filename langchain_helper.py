
from langchain.llms import LLM 
import math
from langchain_google_genai.llms import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import Tool, initialize_agent, load_tools, AgentType 
 

from dotenv import load_dotenv

load_dotenv()

def langchain_agent():
    llm = GoogleGenerativeAI(model='gemini-pro', temperature=0.5)
    tools = load_tools(["llm_math"], llm= llm)


    
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="Answer the following question: {question}" ) 


   

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
                  


    
result = agent.run(prompt_template.format(question="If a dog year is equivalent to 7 human years, how old is a 10-year-old dog in human years?"))
  

result = agent.run("What is 2+2?")

print(result) 

if __name__ == "__main__":
    langchain_agent()

 



    



    






