from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.header("LangChain Prompt Example")

user_input = st.text_input("Enter your prompt here:")

if st.button("Generate Response"):
    st.text("Generating response...")