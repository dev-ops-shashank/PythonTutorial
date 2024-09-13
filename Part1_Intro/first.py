# how do we print anything in the termial? with print() function, and it doesn't have semi-colon :D
print("Hello Earth!")

# in python you don't have to mention the data type for variable in order to assign any value to someting.
text1 = "Python"
print(text1)

# You can also change value of the variable to a different vlaue of different data type and python won't mind it
#try it yourself
text1 = 45
print(text1)

# When starting Python, you must have heard about libraries. They are like a container of different function that 
# we can use without the need to write that login. Ando how can you get that libray, by just importing that.
# here's a funny Library names "PyJokes", you can import it and use its function get_joke()
# before importing that, you need to install this library. For that goto your terminal, write "pip install pyjokes"
import pyjokes
joke = pyjokes.get_joke()
print(joke)

# Commenting is python is easy and helful, you can do that by using '#' symbol. 
# Worrined about commenting multiple lines in your code? you can do that by using 3 single quotes ''', check below
'''
This is a comment
line 2 of comment
'''
# Fun part about these 3 single quotes is you can use it to print multiple lines with a single print() function, check below:
# Note that whatever you write inside it will be printed exactly the same with all the indentation(spaces, tabs, nextlines)
print('''
Printing line 1
Printing line 2
      Printing line 3
''')