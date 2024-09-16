age = int(input("Enter your Age : "))

# Code using nested if-else

# if(age>=0 & age<=100):
#     if (age>=18):
#         print("you are an Adult!")
#         print("You need to be responsible now!")
#     else:
#         print("You are Minor!")
# else:
#     print("Invalid Input, You are not Human! |-_-| ")

# Another way to write this code using if-elif-else (note that elif condition must an ending else condition)

if(age<0):
    print("Invalid Input, You are UnderAge! |-_-| ")
elif(age>110):
    print("Invalid Input, You are OverAge! |-_-| ")
elif (age>=18 and age<=100):
    print("you are an Adult!")
else:
    print("You are Minor!")


print("!!END OF PROGRAM!!")

# Relational Operatiors
# ==
# <=
# >=

# Logical Operator
# and
# or
# not

