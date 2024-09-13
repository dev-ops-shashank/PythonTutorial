list1 = ["Boy", 66.88, 'Akshay', 33, True, "Toy"]
print(list1[2])                                 # Get the lits' item with index
print(list1[-1])
print(f" Original List : {list1}")
list1[2] = 76                                   # modifying the value in list
print(f" New List : {list1}")                   # Lists are muatable
print(list1[3:])                                # Slicing in Lists
list2 = [4,6,23.7,"New"]
list3 = list1 + list2                           # Concatenation of Lists
print(list3)                                
print(list2 * 2)                                # repeating a list

# Fucntions for Lists:

print(len(list3))
# print(list3.sort())   # Error as they are of different types and python can't compare them
list1.reverse()
print(f"Reversed List : {list1}")      #reverse the list

list1.insert(2,"newWord")
print(f"New List 1 after inserting new value in index 2 is : {list1}")

# List Comprehension
sqaures = [x**2 for x in range(5) ]     # for Squares of 0 - 4
print(f"Square of number from 0-4 : {sqaures}")

sqaures = [x**2 for x in range(21) if x % 2 == 0 ]     # for squares of 0 - 20 for even numbers
print(f"Square of even number in range 0-20 : {sqaures}")

sqaures.append(2)
print(f"After appending 2 in this list, the new list is : {sqaures}")

sqaures.pop()
print(f"After popping out the last element from the Square list: {sqaures}")

sqaures.pop(4)
print(f"Popping number at index 4, new list is : {sqaures}")

# sqaures.remove(111)         # ValueError: list.remove(x): x not in list, 111 is not present in the list
sqaures.remove(144)
print(f"After removing 111 from Squares list, the new list is: {sqaures}")
