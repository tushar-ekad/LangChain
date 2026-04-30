from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke('what is happening with us iran war')

print(results)
print(search_tool.name)
print(search_tool.description)
print(search_tool.args)