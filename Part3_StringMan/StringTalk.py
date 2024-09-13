# String is a sequence of character enclosed in quotes.
# We can write String in 3 ways:
# str1 = 'String 1'       # single quote
# str2 = "String 2"       # double quote
# str3 = '''String 3'''   # triple quote

# String are immutable - cannot be changed once created, Ex - str1 cannot be changed to some other value

# str1[3] = 'o'
# print(str1)     # TypeError: 'str' object does not support item assignment

# str1 = 'Python'
# this is not changing the value of string, this is called value reassigning. You are not changing the value of str1, you are 
# creating a new string and assigning that to str1. both are different

# there is predefined method called replace(,) which can help us in mutating(changing) the string
original = "Hello"
modified = original.replace('H', 'J')
print(modified)  # Output: Jello
print(original)  # Output: Hello
# When you use methods like replace(), they don't modify the original string. 
# Instead, they create and return a new string with the requested changes.


# This is a common source of confusion for people new to Python or coming from languages where strings are mutable. 
# In Python, to "mutate" a string, you always end up creating a new string object, even if it 
# seems like you're modifying the original.
# If you want to update the original variable to refer to the new string, you would need to reassign it:
original2 = "Python"
original2 = original2.replace('P', 'J')
print(original2)  # Output: Jello
# But even in this case, you're not mutating the original string object - you're creating a new string
# and updating the variable to refer to this new string