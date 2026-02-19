from langchain_community.tools import ShellTool

tool = ShellTool()

result = tool.invoke('whoami')
print(result)