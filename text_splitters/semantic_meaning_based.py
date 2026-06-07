from  semantic_chunker.core import SemanticChunker
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker()

chunks = [
    {"text": "Artificial intelligence is a growing field."},
    {"text": "Machine learning is a subset of AI."},
    {"text": "Photosynthesis occurs in plants."},
    {"text": "Deep learning uses neural networks."},
    {"text": "Plants convert sunlight into energy."},
]

docs = text_splitter.chunk(chunks=chunks)

print(f"Number of chunks: {len(docs)}")

for i, doc in enumerate(docs):
    print(f"Chunk {i+1}: \n{doc['text']}")
    print()