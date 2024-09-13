# Tuple creation
tuple_num = (34, 55, 77, 12, 44, 69, 55.66)
mixed_tuple = (55, "Dell", True, 44.98, "ASUS")
nested_tuple = (3, (22, 44, 66, 88), 12, 45, 78, 99)
small_tuple = (1, 2, 3, 4, 5, 3, 2, 2, 3)

# Accessing Tuple Elements
print(f"Num Tuple Element at index 3 : {tuple_num[3]}")
print(f"Mixed Tuple Element at index 2 : {mixed_tuple[2]}")
print(f"Nested Tuple Element at index [1][3]: {nested_tuple[1][3]}")

# Slicing Tuples
print(f"Mixed Tupel Elements from index 0 to 2 : {mixed_tuple[0:3]}")

# Immutability
# tuple_num[2] = 65       # TypeError: 'tuple' object does not support item assignment; Immutable

# Tuple Concatination
concat_Tuple = tuple_num+mixed_tuple
print(f"New Tuple after concatination is : {concat_Tuple}")

# Tuple Repeatition
print(f"Repeating small tuple 3 times : {small_tuple*3}")

# Packing & Unpacking Tuples
cordinates = 10, 20, 30 , 40            # packing
w, x, y, z = cordinates                 # unpacking
print(f"Packing-Unpacking : {x,y,z}")

# Tuple Function
print(f"Length of Small Tuple : {len(small_tuple)}")
print(f"Largest element in Num Tuple : {max(tuple_num)}")           # sames goes with min(), sum()
# print(f"Largest element in Mixed Tuple : {max(mixed_tuple)}")      # TypeError: '>' not supported between instances of 'str' and 'int'
# print(f"Largest element in Nested Tuple : {max(nested_tuple)}")      # TypeError: '>' not supported between instances of 'tuple' and 'int'
print(f"Sorting Number Tuple : {sorted(tuple_num)}")
# print(f"Sorting Mixed Tuple : {sorted(mixed_tuple)}")           # TypeError: '<' not supported between instances of 'str' and 'int'
# print(f"Sorting Nested Tuple : {sorted(nested_tuple)}")           # TypeError: '<' not supported between instances of 'tuple' and 'int'
# In order to sort a tuple, all element should be in same data type
tuple_from_list = tuple([3,5,77,12.88,"yes"])
print(f"tuple created from a list : {tuple_from_list}")
print(f"Times '2' appear in Small Tuple : {small_tuple.count(2)}")
print(f"Returns the index of the first occurrence of the element '3' in Small tuple : {small_tuple.index(5)}")


