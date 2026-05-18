from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Hello, how are you?"

vector = embedding.embed_query(text)

print(f"Query Vector: {str(vector)}")

documents = ["Hello, how are you?", 
             "What is your name?", 
             "Where are you from?"]

document_vectors = embedding.embed_documents(documents)

print(f"Document Vectors: {str(document_vectors)}")