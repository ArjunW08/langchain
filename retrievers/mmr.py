from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Step 1: Your source documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

vector_store = FAISS.from_documents(docs, embedding_model)

retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.3}
)

query = "What is LangChain?"
retrieved_docs = retriever.invoke(query)

print(f"Number of documents retrieved: {len(retrieved_docs)}")

for i, doc in enumerate(retrieved_docs):
    print(f"Document {i+1}: \n{doc.page_content}\n")
