from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke('US, Iran war news today')

print(f"Details about {search_tool}\nTool Name : {search_tool.name}\nTool Description : {search_tool.description}\nTool Args : {search_tool.args}")

print(results)