from langchain.tools import tool

@tool
def multply(a:int, b:int) -> int:
    "Multiply two numbers"
    return a * b

@tool
def addition(a:int, b:int) -> int:
    "Addition of two numbers"
    return a + b

class MathToolkit:
    def get_tools(self):
        return (addition, multply)
    
toolkit = MathToolkit()
tools = toolkit.get_tools()

for tool in tools:
    print(tool.name, tool.description)