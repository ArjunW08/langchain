from langchain_community.tools import ShellTool

shell_tool = ShellTool()

results = shell_tool.invoke('ls')

print(f"Details about {shell_tool}\nTool Name : {shell_tool.name}\nTool Description : {shell_tool.description}\nTool Args : {shell_tool.args}")

print(results)