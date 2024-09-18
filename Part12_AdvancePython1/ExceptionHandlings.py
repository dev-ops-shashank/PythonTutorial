'''def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
try:
    validate_age(-5)
except ValueError as e:
    print(e)'''

class CustomError(Exception):
    pass

def my_function(value):
    if value < 0:
        raise CustomError("Value cannot be negative")
try:
    my_function(-1)
except CustomError as e:
    print(f"Caught custom exception: {e}")
