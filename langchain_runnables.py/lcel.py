from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.schema.runnable import RunnablePassthrough, RunnableBranch
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following: \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

report_gen_chain = prompt1 | model | parser

def word_counter(text):
    return len(text.split())

branch_chain = RunnableBranch(
    (word_counter>500, prompt2 | model | parser),
    RunnablePassthrough()
)

chain = report_gen_chain | branch_chain

result = chain.invoke({'topic': 'DNA'})

print(result)