from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a fictional person. /n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()} # uses additional instructions from parser
)

# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

chain = template | model | parser

final_result = chain.invoke({})
print(final_result)