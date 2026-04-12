from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate short and simple notes on the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template = 'Generate 5 short questions-answers on following text. /n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template = 'Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

model1 = ChatOpenAI()
model2 = ChatAnthropic(model_name='claude-3-7-sonnet-20250219')

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 |parser

chain = parallel_chain | merge_chain

text = """
LangChain's developers highlight the framework's applicability to use-cases including chatbots, retrieval-augmented generation, document summarization, and synthetic data generation. InfoWorld described LangChain as a software development kit that simplifies the connection between large language models and external applications through a unified API. The magazine also wrote that it can be used to bring in context from sources such as PDFs, web pages, CSV files and relational databases, while making it easier for developers to change the underlying model without major code changes.

As of March 2023, LangChain included integrations with systems including Amazon, Google, and Microsoft Azure cloud storage; API wrappers for news, movie information, and weather; Bash for summarization, syntax and semantics checking, and execution of shell scripts; multiple web scraping subsystems and templates; few-shot learning prompt generation support; finding and summarizing "todo" tasks in code; Google Drive documents, spreadsheets, and presentations summarization, extraction, and creation; Google Search and Microsoft Bing web search; OpenAI, Anthropic, and Hugging Face language models; iFixit repair guides and wikis search and summarization; MapReduce for question answering, combining documents, and question generation; N-gram overlap scoring; PyPDF, pdfminer, fitz, and pymupdf for PDF file text extraction and manipulation; Python and JavaScript code generation, analysis, and debugging; Milvus vector database to store and retrieve vector embeddings; Weaviate vector database to cache embedding and data objects; Redis cache database storage; Python RequestsWrapper and other methods for API requests; SQL and NoSQL databases including JSON support; Streamlit, including for logging; text mapping for k-nearest neighbors search; time zone conversion and calendar operations; tracing and recording stack symbols in threaded and asynchronous subprocess runs; and the Wolfram Alpha website and SDK. As of April 2023, it can read from more than 50 document types and data sources.
"""

result = chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()