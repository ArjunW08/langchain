from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0:featherless-ai",
#     task="text-generation",
# )

# model = ChatHuggingFace(llm=llm)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 1st Prompt -> detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}.",
    input_variables=['topic']
)


# 2nd Prompt -> concise summary
template2 = PromptTemplate(
    template="Write a 5 pointer summary on the following text. \n {text}",
    input_variables=['text']
)

# prompt1 = template1.invoke({'topic': 'shivaji maharaj'})

# result = model.invoke(prompt1)

# prompt2 = template2.invoke({'text': result.content})

# result1 = model.invoke(prompt2)

# print(result1.content)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'shivaji maharaj'})

print(result)