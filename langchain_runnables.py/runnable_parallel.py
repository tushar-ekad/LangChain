from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.schema.runnable import RunnableParallel, RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a LinkedIn post about \n {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1, model, parser),
    'linkedin_post':RunnableSequence(prompt2, model, parser)
})

result = chain.invoke({'topic':'Generative AI'})

print(result)
print(result['tweet'])