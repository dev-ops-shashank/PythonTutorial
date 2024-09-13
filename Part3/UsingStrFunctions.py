
str1 = "Hello {} {} {} {}"
str2 = "Python"
str3 = "BOOTCAMP4356"
str4 = "Python2024+-@#4"
abc = "functions\tare\tuseful\tin\tpython"

name = "Guido_van_Rossum"
#  G   u   i   d   o   _   v   a  n  _  R  o  s  s  u  m
#  0   1   2   3   4   5   6   7  8  9  10 11 12 13 14 15
# -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1


print(abc.capitalize())
print(str3.casefold())
print(f"'{str1.center(20)}'") # If the width is less than or equal to the length of the string, no centering occurs, and the original string is returned.
print(str3.count("O"))
print(str1.encode("utf-16"))
print(str3.endswith('6'))
print(str1.startswith('b'))
print(f"'{abc.expandtabs(4)}'") # starting from left, it will calculate length, and move in steps of 4. it will go like in the string
# until it finds a '\t' and than include number of spaces there. by default, value is 8
# for string "Rajesh\tis\ta\tBoy", from left R(1)a(2)j(3)e(4)s(5)h(6)\t(7), now 'Raje' are 4 character, it will start from 'sh' 2 character after which \t came. so 4-2=2, 2 spaces will be added(because we mentioned 4 in expandtabs() function).
print(f"letter 'o' found at postion : {abc.find('o')+1}")
print(str1.format("hello","kya","haal","dosto")) # works similar to f"" in printf
person = {"name": "Alice", "age": 30}
print("My name is {name} and I am {age} years old".format_map(person)) # works same as format() but with dictionary of the values
print(f"letter 'R' found at postion : {name.index("R")+1}")
print(str3.isalnum()) # True  print(str4.isalnum()) # False
print(str3.isalpha()) # False  print(str2.isalpha()) # True
print("123".isdecimal(), "123".isdigit(), "123".isnumeric())  # True True True
print("①".isdecimal(), "①".isdigit(), "①".isnumeric())  # False True True
print("½".isdecimal(), "½".isdigit(), "½".isnumeric())  # False False True
print(abc.replace("functions","Libraries"))
print("Hello\tWorld".isprintable()) # False if any character in the string cannot be displayed in the output


