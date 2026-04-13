from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.schema.runnable import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough
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

def word_counter(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)
joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_counter)
})

chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = chain.invoke({'topic': 'monkey'})

print(result)