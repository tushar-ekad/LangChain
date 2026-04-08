from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6_v2')

text = "what is the capital of India"

vector = embedding.embed_query(text)

print(str(vector))