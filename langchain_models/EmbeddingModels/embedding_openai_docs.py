from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions = 32)

documents = [
    "my name is peter",
    "delhi is capital of india"
]

result = embedding.embed_documents(documents)

print(str(result))