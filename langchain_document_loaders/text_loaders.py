from langchain_community.document_loaders import TextLoader

loader = TextLoader("D:\\notepad++\\question_bank\\fastapi-streamlit-unittest-ques.txt", encoding='utf-8')

docs = loader.load()

print(docs)