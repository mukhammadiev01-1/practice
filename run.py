# Dunder __builtins__, __init__
message = "PYTHON: Everything is object!"
print(message)
#dunder is a special method that starts and ends with double underscores
#dunders function is to provide special functionality to the objects
#dunder's definition is in C language and implemented in Python's core

result = type(message)
print("result:", result)

''' In Python, there are builtin tools:
 (1) TYPES > int float str list dict
 (2) FUNCTIONS > print() len() input() type()
 (3) CONSTANTS > True False None
'''

print(dir(__builtins__))
