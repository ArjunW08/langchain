from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

# If you print this it will show the prompt template and not replace the variable values into it.
# chat_template = ChatPromptTemplate([
#     SystemMessage(content="You are a helpful {domain} expert."),
#     HumanMessage(content="Explain in simple terms, What is {topic}?")
# ])

chat_template = ChatPromptTemplate(
    [
        ('system', "You are a helpful {domain} expert."),
        ('human', "Explain in simple terms, What is {topic}?")
    ]
)

prompt = chat_template.invoke(input={"domain": "machine learning", "topic": "overfitting"})

print(prompt)