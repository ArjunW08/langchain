from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report on the topic of {topic}.", 
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following text: {text}", 
    input_variables=["text"]
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

report_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 10, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_chain, branch_chain)

result = final_chain.invoke({"topic": "climate change"})

print(result)