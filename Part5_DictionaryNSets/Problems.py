# Q1. WAP to create a dictionary of Hindi words with values as their English translation. Provide User with an option to look it up.
# words = {
#     "namaste" : "Greetings",
#     "kitaab" : "book",
#     "vigyaan" : "science",
#     "dhurbash" : "telephone"
# }

# word = input("Enter a word in hindi ONLY from below options\n\"namaste\" \"kitaab\" \"vigyaan\" \"dhurbash\" \n")

# print(f"English meaning of {word} is {words[word]}")

# Q2 WAP to Input five numbers from the user and display all the unique numbers(once)
# setOfNum = set()
# num = int(input("Enter a number : "))
# setOfNum.add(num)
# num = int(input("Enter a number : "))
# setOfNum.add(num)
# num = int(input("Enter a number : "))
# setOfNum.add(num)
# num = int(input("Enter a number : "))
# setOfNum.add(num)
# num = int(input("Enter a number : "))
# setOfNum.add(num)

# print(setOfNum)

# # Q3. WAP a program to take fav food value from 4 different users.
# foods = {"Raj": "pea", "Ron" : "Apple", "Fed" : "Peach", "Raj" : "Banana"}
# print(foods)            # Raj's value was updated as Raj was re-entered again in last of dict, which overpowered the first Raj value

# Q4. Can you change the value inside a list which is contained in set S? {8, 7, 12, 'Sha', [1, 2]}
S = {8, 7, 12, 'Sha', [1, 2]}
print(S)            # TypeError: unhashable type: 'list'
# This Set is actually not a valid Python set. Here's why:
# Sets can only contain hashable (immutable) elements.
# Lists are mutable, and therefore not hashable.
# Attempting to create this set would raise a TypeError.

# If you try to create this set in Python, you'll get an error like this:
# pythonCopyTypeError: unhashable type: 'list'
# This error occurs because sets in Python require all their elements to be hashable, which essentially means they must be immutable. 
# Lists, being mutable, cannot be elements of a set.
# Given this constraint, there's no way to directly update a list within a set, because such a set cannot exist in the first place.
# However, if you need to store mutable data structures like lists within a set-like structure, you have a few options:

# Use a tuple instead of a list:
# pythonCopyS = {8, 7, 12, 'Sha', (1, 2)}
# But note that tuples are immutable, so you can't modify their contents.
# Use a frozenset to store immutable versions of your data:
# pythonCopyS = frozenset([8, 7, 12, 'Sha', frozenset([1, 2])])
# But again, frozensets are immutable.
# If you really need to store and modify lists, you might need to use a different data structure altogether, such as a list of lists 
# or a dictionary.

