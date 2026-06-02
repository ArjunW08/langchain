from langchain_docling.loader import DoclingLoader

loader = DoclingLoader("/Users/arjun-18888/Personal/langchain/document_loaders/dl-curriculum.pdf")

docs = loader.load()

print(len(docs))

print(docs[1].page_content)
print(docs[1].metadata)