from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama
import streamlit as st
import os

'''Prompt Template'''

prompt = ChatPromptTemplate.from_messages(
    [
        ( 
            "system",
            "You are an expert in data science and a helpful assistant. Your task is to provide clear, concise, and easy-to-understand responses to the user."
        ),
        ("user", "Question: {question}"),  
    ]
)

"streamlit Framework"
st.title("LLM basics using OLLAMA")
input_text= st.text_input("search the topic you want")

"ollama model"
llm = Ollama(model="llama2")




output_parser= StrOutputParser()
chain=prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))