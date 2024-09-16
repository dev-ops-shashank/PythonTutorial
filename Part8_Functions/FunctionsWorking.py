# defining a function
# taking 2 number from user and return num1**num2 using function
'''
def power(num1,num2):
    return f"{num1} to the power {num2} is : {num1**num2}"

def greet(name):
    print("Hello", name)

greet("Shashank")
s = greet("Raj")                            
print(s)                                    # this will give "None" as output as the function is not returning anything
n1 = int(input("Enter First number : "))
n2 = int(input("Enter Second number : "))
print(power(n1,n2))
s = power(5, 2)
print(s)                                    # this does not give "None" as the function was returning some value
'''
# basically functions are used to separate the rule that might be used multiple times on the code
# a single function can be used multiple times in the code

#########################################################################################################
'''
# default values in function:
def greet(name, end="Good evening!"):               # 'end' has a default value which is used when no 2nd argument is providing 
    print("Hello", name, end)                       # in function call

greet("Shashank")                   # Output: "Hello Shashank Good evening!" no end argument is provided here
greet("Shashank", "Happy Monday!")   # Output: "Hello Shashank Happy Monday!" note how end value changes here
'''
#########################################################################################################

# Recursion
# to uderstand recursion, let's take factorial as an example

def factorial(n):
    if n<0:
        return "Invalid Input. Use only positive numbers!!"
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)           # this is what a recursion is. alternative of loops you can say

num = int(input("Enter a Number for which you need to find the factorial : "))
print(factorial(num))