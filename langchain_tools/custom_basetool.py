from langchain_classic.tools import BaseTool
from typing import Type
from pydantic import Field, BaseModel

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to multiply")
    b: int = Field(required=True, description="The second number to multiply")

class MultiplyTool(BaseTool):
    name: str = "Multiplication"
    description: str = "Multiply two numbers"
    args_schema: Type[BaseModel] = MultiplyInput
    
    def _run(self, a: int, b: int) -> int:
        return a * b

multiply_tool = MultiplyTool()

result = multiply_tool.invoke({'a': 5, 'b': 4})
print(result)