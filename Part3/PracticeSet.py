# Q1) Write a python program to display a user entered name followed by "Good Afternoon" using input()
# name = input("Enter your Name: ")
# print(f"Good Afternoon {name}")


# Q2) Write a program to detect a double space in string
# str1 = "Hello there  new boy  in python"
# print(str1.find("  ")) # if returns -1 then there is no substring in the string


# Q3) You are given a string containing a person's full name in the format "firstname lastname". Your task is to create 
# a function that reformats the name to "Lastname, F." where F is the first initial of the first name.

name = "Tom Cruise"
newName = name.title()
first, second = newName.split()
print(f"{second[0]}, {first}")