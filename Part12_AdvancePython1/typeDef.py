# Some more type hints recently added in Python
# from typing import List, Tuple, Dict, Union 
# Works same is type Definition for prmitive data types.
# These annotations helps in making the code self-documenting and allow developers to 
# understand the data structures at a glance.


'''# a) Variable type hints:
age: int = 30
name: str = "Alice"
is_student: bool = True

# b) Function with type hints:
def greet(name: str) -> str:
    return f"Hello, {name}!"

# c) More complex types:
from typing import List, Dict, Optional

def process_data(items: List[int], config: Dict[str, str]) -> Optional[float]:
    # function body
    pass
'''

age1: int = input("Enter your age : ")
print(f"Your Age is : {age1} & its class is {type(age1)}")
# if string is entered, it will give string in output, as input() takes a string value only
# you need to explicitly type convert it to desired data type.
age2 = input("Enter your age2 : ")
print(f"Your Age is : {age2} & its class is {type(age2)}")

age3 = int(input("Enter your age2 : "))
print(f"Your Age is : {age3} & its class is {type(age3)}")
# if entered a string here, it will give ValueError: invalid literal for int()

print(age1.bit_length())    # age1. gives all integer methods, although provided string as input
# funny thing here, I type defined age1 as int, and provided a string value to it. So python now treats
# it as a string only and no int functions will be used with age. 
# AttributeError: 'str' object has no attribute 'bit_length'
# print(age1.capitalize())    # this will work properly
print(age2.capitalize())    # age2. gives all string methods
print(age3.bit_length())    # age3. gives all integer methods

# Remember, type hints are primarily for documentation, static analysis, and developer tooling. 
# They don't change Python's dynamic typing nature at runtime. To ensure type safety in input 
# scenarios, you need to add explicit type conversion and error handling in your code.