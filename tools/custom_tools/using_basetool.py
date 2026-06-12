from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(json_schema_extra={'required' : True}, description="First number to add")
    b: int = Field(json_schema_extra={'required' : True}, description="Second number to add")

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two numbers"

    arg_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b
    
multiply_tool = MultiplyTool()

result = multiply_tool.invoke({'a' : 3, 'b' : 3})

print(result)
print(multiply_tool.name)
print(multiply_tool.description)

print(multiply_tool.args)