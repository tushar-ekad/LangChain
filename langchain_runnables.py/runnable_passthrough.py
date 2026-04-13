from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.schema.runnable import RunnablePassthrough, RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke: \n {joke}',
    input_variables=['joke']
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke_explain': RunnableSequence(prompt2, model, parser),
    'joke': RunnablePassthrough()
})

chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = chain.invoke({'topic':'developer'})

print(result)