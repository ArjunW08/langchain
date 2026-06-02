from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="/Users/arjun-18888/Personal/langchain/document_loaders/books",
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for doc in docs:
    print(doc.metadata)