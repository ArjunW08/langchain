import wikipedia
from langchain_community.retrievers import WikipediaRetriever

wikipedia.set_user_agent("MyLangChain")

retriever = WikipediaRetriever(top_k_results=3, lang="en")

query = "the geopolitical history of india and pakistan from the perspective of a chinese"

docs = retriever.invoke(query)

print(f"Number of documents retrieved: {len(docs)}")

for i, doc in enumerate(docs):
    print(f"Document {i+1}: \n{doc.page_content}\n")