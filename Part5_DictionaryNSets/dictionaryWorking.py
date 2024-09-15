# Empty Dictiionary: empty_marks = {}
# Decalring Dictionary
marks = {"Hola" : 34, "Bhuvan" : 78, "Sameer" : 98, 45 : "reverse" }
print(f"Marks of everyone\t{marks} \nData Type of Marks is\t{type(marks)}")
# Accessing the Value from key
print(f"Marks of Bhuvan\t: {marks["Bhuvan"]}")

# Basic methods of Dictionary
print(marks.items())    # gets all the items in dictionary
print(marks.keys())     # gets all the keys in dictionary
print(marks.values())   # gets all the values in dictionary

# Updating a Dictionary : Dictionaries are mutable
marks.update({45 : 99, "Hola" : 99})
print(marks)
marks.update({"Ram" : 100})
print(marks)
# del marks["Ram"]        # deleting a key-value
marks.popitem()           # remove last added item
print(marks)

# get() usage in dictionary
print(marks.get("Ashish"))      # returns 'None' as there is no key as Ashish
print(marks.get("Ashish", 0))   # retunrs 0 if there is no key "Ashish"
print(marks.get("Bhuvan"))      # reutrns 78
print(marks.get(45))            # returns 99
print(marks[45])                # returns 99
# print(marks[44])                # returns error
# Notice one thing marks[44] give error, while marks.get("Ashish") gives None, when both the key does not exist in marks{}
# * Square brackets [] raise an exception for non-existent keys.
# # * get() method returns None for non-existent keys (by default).
# Use [] when you're sure the key exists and want an error if it doesn't.
# Use get() when you want to handle missing keys gracefully without exception handling.
# [] notation is slightly faster, but the difference is negligible in most cases.
# In practice, using get() is often preferred when you're not certain if a key exists and you want to avoid exception handling. 
# It's particularly useful in situations where you're dealing with user input or data from external sources where the presence 
# of a key is not guaranteed.

# marks.clear()       # clear all items
# print(marks)


## Nested Dictionary
employees = {
    "John": {"age": 30, "position": "Manager"},
    "Alice": {"age": 25, "position": "Developer"}
}
print(employees["John"]["position"])  # Output: Manager

## Merging 2 dictionaries
dict1 = {'a' : 12, 'b' : 11, 'c' : 45}
dict2 = {'p' : 22, 'q' : 21, 'r' : 55}
merged = {**dict1, **dict2}
# merged = dict1 + dict2      # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
print(merged)

