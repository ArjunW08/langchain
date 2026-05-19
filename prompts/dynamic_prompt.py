from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

st.header("LangChain Dynamic Prompt Example")

paper_input = st.selectbox("Select a research paper:", ["Select...", "Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models in Computer Vision: A Survey"])

style_input = st.selectbox("Select Explanation Style:", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length:", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (Detailed Explanation)"])

if st.button("Summarize Paper"):
    st.text("Generating summary...")
    prompt = f"Summarize the research paper '{paper_input}' in a {style_input} style with a {length_input} length."
    response = model.invoke(prompt)
    st.text_area("Summary:", value=response.content, height=300)