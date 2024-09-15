empty_set = set()       # Empty Set Declaraction; Don't use empty set with = {} as it will create a dictionary
set1 = {3, 6, 7, 8, 12, 'harold'} # Initialization; Set with some value, looks a bit same as list (difference of {} [])
setDup = {45, 12, 23, 23, 45, 11, 10, "Harold", 'Harold', 'harold'}
print(setDup)       # removed the duplicate value from the set; returns unordered set

# Methods in set
set1.add("set")         # adding element is set
print(set1)
# set1.clear()          # Remove all elements from the set
# How copy() Works:
# When you call copy() on a set, Python creates a new set object.
# The new set contains references to the same objects that are in the original set.
# The new set is independent of the original set (you can add or remove elements from one without affecting the other).
set_copy = set1.copy()
print(set_copy)
set1.add(45)
print(set1)
print(len(set1))        # returns length of the set1
set1.remove(6)
print(set1)             # removed element 6 from set1
print(setDup.pop())     # removes an arbitary element and return the element removed
print(setDup)
print(type(setDup))

# Operations in Sets
print(f"Union of Set {set1.union(setDup)}")
print(f"Intersection of Set {set1.intersection(setDup)}")

# Anothere ways of Operations in Sets
myset1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"\n\nUnion : {myset1 | set2}")  # Union
print(f"Intersection : {myset1 & set2}")  # Intersection
print(f"Difference : {myset1 - set2}")  # Difference
print(f"Difference2 : {set2 - myset1}")  # Difference type 2
print(f"Symmetric Difference : {myset1 ^ set2}")  # Symmetric difference

# there are many methods in sets, you can try them on your own. Take reference from "SetTalking.txt" file