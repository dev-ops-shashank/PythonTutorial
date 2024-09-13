
# ########################################################################################################################################
# Here's a comprehensive list of the built-in string methods in Python:

# 1. `capitalize()`: Converts the first character to upper case
# 2. `casefold()`: Converts string into lower case
# 3. `center()`: Returns a centered string. used to center-align a string within a specified width.It returns a new string padded with spaces (or a specified character) on both sides to center the original string.
# 4. `count()`: Returns the number of times a specified value occurs in a string
# 5. `encode()`: Returns an encoded version of the string, used to encode the string using the specified encoding. It returns a bytes object representing the encoded string.
# 6. `endswith()`: Returns true if the string ends with the specified value
# 7. `expandtabs()`: used to expand tab characters ('\t') in a string into spaces. It returns a new string where all tab characters are replaced with whitespace.
# 8. `find()`: Searches the string for a specified value and returns the position
# 9. `format()`: Formats specified values in a string
# 10. `format_map()`: Formats specified values in a string
# 11. `index()`: Searches the string for a specified value and returns the position
# 12. `isalnum()`: Returns True if all characters in the string are alphanumeric
# 13. `isalpha()`: Returns True if all characters in the string are in the alphabet
# 14. `isascii()`: Returns True if all characters in the string are ascii characters
# 15. `isdecimal()`: Returns True if all characters in the string are decimals
# 16. `isdigit()`: Returns True if all characters in the string are digits
# 17. `isidentifier()`: Returns True if the string is an identifier
# 18. `islower()`: Returns True if all characters in the string are lower case
# 19. `isnumeric()`: Returns True if all characters in the string are numeric
# 20. `isprintable()`: Returns True if all characters in the string are printable
# 21. `isspace()`: Returns True if all characters in the string are whitespaces
# 22. `istitle()`: Returns True if the string follows the rules of a title
# 23. `isupper()`: Returns True if all characters in the string are upper case
# 24. `join()`: Converts the elements of an iterable into a string
# 25. `ljust()`: Returns a left justified version of the string
# 26. `lower()`: Converts a string into lower case
# 27. `lstrip()`: Returns a left trim version of the string
# 28. `maketrans()`: Returns a translation table to be used in translations
# 29. `partition()`: Returns a tuple where the string is parted into three parts
# 30. `replace()`: Returns a string where a specified value is replaced with a specified value
# 31. `rfind()`: Searches the string for a specified value and returns the last position
# 32. `rindex()`: Searches the string for a specified value and returns the last position
# 33. `rjust()`: Returns a right justified version of the string
# 34. `rpartition()`: Returns a tuple where the string is parted into three parts
# 35. `rsplit()`: Splits the string at the specified separator, and returns a list
# 36. `rstrip()`: Returns a right trim version of the string
# 37. `split()`: Splits the string at the specified separator, and returns a list
# 38. `splitlines()`: Splits the string at line breaks and returns a list
# 39. `startswith()`: Returns true if the string starts with the specified value
# 40. `strip()`: Returns a trimmed version of the string
# 41. `swapcase()`: Swaps cases, lower case becomes upper case and vice versa
# 42. `title()`: Converts the first character of each word to upper case
# 43. `translate()`: Returns a translated string
# 44. `upper()`: Converts a string into upper case
# 45. `zfill()`: Fills the string with a specified number of 0 values at the beginning

# Here are a few key points about these functions:

# These methods are called on string objects. For example: "hello".upper() would return "HELLO".
# Some methods like find(), index(), rfind(), and rindex() return positions in the string. The difference is that index() and rindex() raise an exception if the substring is not found, while find() and rfind() return -1.
# Methods like isalpha(), isdigit(), islower(), isupper(), etc., return boolean values (True or False) based on the condition they're checking.
# The format() method is very powerful for string formatting and is often used as an alternative to f-strings or the older %-formatting.
# Some methods like split(), rsplit(), and partition() return lists or tuples, which can be useful for string parsing.
# Methods like strip(), lstrip(), and rstrip() are commonly used for cleaning up strings, removing whitespace or specified characters from the ends of strings.

# Remember that strings in Python are immutable, which means these methods don't change the original string. Instead, they return a new string with the changes applied.