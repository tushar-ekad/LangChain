from langchain_community.document_loaders import PyPDFLoader

# mostly text PyPDFLoader
loader = PyPDFLoader('your-pdf-path')

docs = loader.load()

print(docs)
print(docs[0].page_content)
print(docs[0].metadata)