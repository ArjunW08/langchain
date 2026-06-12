from langchain_core.tools import tool

# Step 1 : create a function
# Step 2 : add type hints
# Step 3 : add a tool decorator
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a*b

print(f"Details about Multiply Tool\nTool Name : {multiply.name}\nTool Description : {multiply.description}\nTool Args : {multiply.args}")

result = multiply.invoke({"a":3, "b":5})

print(result)