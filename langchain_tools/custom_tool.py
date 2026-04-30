from langchain.tools import tool

# 1. add @tool decorator
# 2. create function with your logic
# 3. add type hints and docstring to the function 
@tool
def multply(a:int, b:int) -> int:
    "Multiply two numbers"
    return a * b

result = multply.invoke({"a": 3, "b": 5})
print(result)
print(multply.name)
print(multply.description)
print(multply.args)