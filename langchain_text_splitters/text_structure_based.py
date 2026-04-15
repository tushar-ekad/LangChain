# from langchain.text_splitter import CharacterTextSplitter
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("langchain_text_splitters/dl-curriculum.pdf")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0
)

result = splitter.split_documents(docs)

print(len(result))
print(result[1].page_content)