# Below are the Mathematical Operators used in Python
# Arithmetic Operators : -, +, *, /, //, **, etc
# Assignment Operators : =, +=, -=, *=, /=, etc
# Comparison Operators : ==, >=, <=, <, >, !=, etc
# Logical Operators : and, or, not
print(12+77)    #prints 89
print(12/5)     #prints 2.4, returns float number
print(12//5)    #prints 2, return integer after removing all the numbers after decimal in result. note: this does not do the roundOff
print(3*2)      #prints 6, simply returns the multiple
print(3**2)     #prints 9, returns 3 to the power 2, Exponential

# type casting: converting one type to another if the value is of the new type only
# Ex: to convert INT type to Float, we can do that by :
x=10
y = float(x)
print(type(x))
print(type(y))

# but if we try to convert string to integer, it will give us error:
# a = "sha"
# b = int(a)  # ValueError: invalid literal for int() with base 10: 'sha'
# print(type(a))
# print(type(b))

# below will work as we are converting a float value, which is inside a str variable, to a float integer variable
a = "31.5"
b = float(a)  # this will work fine
print(type(a))
print(type(b))

# In next SubPart, we will create a small Calculator using these operators.
