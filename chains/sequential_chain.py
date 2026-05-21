from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate a detailed report about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following report in 5 points: {report}",
    input_variables=["report"]
)

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "the moon"})

print(result)

chain.get_graph().print_ascii()