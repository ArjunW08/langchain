from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load environment variables from .env file
load_dotenv()

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    output_dimensionality=768
)

query = "Tell about Rohit"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)[0]

print(query)
print(documents[index])
print(f"Similarity Score: {score}")