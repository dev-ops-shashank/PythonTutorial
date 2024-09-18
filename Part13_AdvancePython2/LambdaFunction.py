# lamda fucntion is like a inline function where all the definition of a fucntion is written in line 
# without defining the fucntion explicitly

'''def square(n):
    print(n**2)
square(5)'''

# this can also be written using lambda function
Square = lambda x: x**2
print(Square(5))