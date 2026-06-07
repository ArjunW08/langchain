from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
vector_store = Chroma(
    collection_name="cricket_players",
    embedding_function=embeddings)    

documents = [
    Document(
        page_content="Sachin Tendulkar is a former Indian cricketer widely regarded as one of the greatest batsmen in the history of cricket.",
        metadata={"Team": "Mumbai Indians"}
    ),
    Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"Team": "Mumbai Indians"}
    ),
    Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"Team": "Chennai Super Kings"}
    ),
    Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"Team": "Mumbai Indians"}
    ),
    Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"Team": "Chennai Super Kings"}
    )
]

vector_store.add_documents(documents)

print(f"Retrieved documents: \n\n{vector_store.get(include=['metadatas', 'documents', 'embeddings'])}\n\n")

print(f"Best Bowler: \n\n{vector_store.similarity_search(query='Who is the best bowler?',k=2)}")

print(f"Best Bowler: \n\n{vector_store.similarity_search_with_score(query='Who is the best bowler?',k=2)}")

print(f"{vector_store.similarity_search_with_score(query=' ',filter={'Team': 'Mumbai Indians'}, k=3)}")