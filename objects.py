''' OBJECTS
    (1) What is object
    (2) Iterable objects & RANGE 
    (3) DICTIONARY
    (4) Error handling system
'''

import array  # package/module
import math  # package
from math import ceil
print("===== What is object =====")
# An object has state and method properties.
# Everything is object in Python!

print(type('Hello World!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP
# OOP 4 CONCEPTS > Abstraction | Encapsulation | Inheritence | Polimorphism
result1 = math.ceil(97.7)  # CALL round up the number to the nearest integer
print("result1:", result1)

result2 = ceil(98.7)
print("result2:", result2)


print("===== Error handling system =====")
# in javascript > const car = {name: "Tayota", year: 2026, electric: true}
car_dict = dict(name="Tayota", year=2026, electric=True)

try:
    print("passed here")
    result = car_dict["origin"]
    print("result:", result)
except Exception as err:
    print("General Error:", err)
else:
    print("Executed successfully without errors")
finally:
    # always executed, even if there is an error or not
    print("Final closing logic")

# {} is used in classes in Javascript, but in Python we use indentation to define the scope of classes, functions, loops, etc.


# indentation error > SyntaxError
# multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# python also has destructuring but called unpacking
