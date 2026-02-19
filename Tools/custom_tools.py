from langchain_core.tools import tool

@tool
def pyramid(n : int) ->int :
    """ This function make star pattern"""
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    return "Star pattern"

result = pyramid.invoke({'n':5})
print(result)