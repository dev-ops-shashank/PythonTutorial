# Similar to Switch cases in Java.
# this mostly requires a function to implement this
# this feature is only available in Python 3.10 and later versions
def describe_type(value):
    match value:
        case int():
            print("It's an integer")
        case str():
            print("It's a string")
        case list():
            print("It's a list")
        case _:                             # Similar to Default in Switch cases' default case
            print("It's something else")

describe_type(42)        # Output: It's an integer
describe_type("hello")   # Output: It's a string
describe_type([1, 2, 3]) # Output: It's a list
describe_type(3.14)      # Output: It's something else