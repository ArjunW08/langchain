from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}.", 
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Write a poem about {topic}.", 
    input_variables=["topic"]
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

joke_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel(
    {
        'joke' : RunnablePassthrough(),
        'explanation' : RunnableSequence(prompt2, model, parser)
    }
)

final_chain = RunnableSequence(joke_chain, parallel_chain)

print(final_chain.invoke({"topic": "cricket"}))
