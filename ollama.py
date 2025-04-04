LANGCHAIN_API_KEY="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"
# #OPENAI_API=""
LANGCHAIN_PROJECT="Q&AChatbot"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

##environment variables call
##os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


##Langsmith tracking
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
os.environ["LANGCHAIN_TRACING_V2"]="true"

##creating chatbot

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please provide response to the user queries"),
    ("user", "Question: {question}")
])


#streamlit framework

st.title("Langchain Demo With LLama2 API")
input_text=st.text_input("Search the topic you want")

#open AI LLM call
llm=Ollama(model="llama2")
output_parser=StrOutputParser()

##chain
chain=prompt|llm|output_parser



if input_text:
    st.write(chain.invoke({'question':input_text}))



