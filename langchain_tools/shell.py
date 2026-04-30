from langchain_community.tools import ShellTool

shell_tool = ShellTool()

results = shell_tool.invoke('whoami')

print(results)
print(shell_tool.name)
print(shell_tool.description)
print(shell_tool.args)