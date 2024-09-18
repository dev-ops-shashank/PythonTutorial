# map() applies a function to all items in an input list.
l = [1, 2, 3, 4, 5, 6]
# I want to make square list of this list
square = lambda x: x**2
# syntax: map(function_name, input_list)
sqList = map(square,l)
print(sqList)               # this gives output <map object at 0x000002755E78B9A0>
print(list(sqList))         # this will convert the sqlist to list and returns desired list

####################################
####################################

#filter() filters out the values from a list
l = [1, 2, 3, 4, 5, 6]
def even(n):
    if(n%2==0):
        return True
    return False
# syntax: map(function_name, input_list)
onlyEven = filter(even, l)
print(list(onlyEven))

####################################
####################################

# reduce() applies a rolling computation to sequential pair of elements
# it similar to recursion if used properly
from functools import reduce
print(l)
sum = lambda a,b: (a+b)
mul = lambda a,b: (a*b)
print(reduce(sum, l))
print(reduce(mul, l))