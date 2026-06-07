from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders.pdf import PyPDFLoader

loader = PyPDFLoader("text_splitters/dl-curriculum.pdf")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, 
                                      chunk_overlap=0,
                                      separator=" ")

result = text_splitter.split_documents(documents)
print(f"Number of chunks: {len(result)}")
print(result[1].page_content)