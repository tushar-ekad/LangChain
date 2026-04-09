from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give me 3 facts about {topic} /n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'topic': 'black hole'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

chain = template | model | parser

final_result = chain.invoke({'topic': 'black hole'})

print(final_result)