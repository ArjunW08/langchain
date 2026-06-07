from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Step 1: Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

vector_store = Chroma.from_documents(
    documents,
    embedding=embedding_model,
    collection_name="my_collection",
)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

query = "What is LangChain?"
retrieved_docs = retriever.invoke(query)

print(f"Number of documents retrieved: {len(retrieved_docs)}")
for i, doc in enumerate(retrieved_docs):
    print(f"Document {i+1}: \n{doc.page_content}\n")

