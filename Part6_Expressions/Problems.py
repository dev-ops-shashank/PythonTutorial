# Q1. WAP to find out whether a student has passed or failed if it requires a total 40% and atleast 33% in each subject to pass.
# Assume 3 subjects and take input from user 
# mark1 = int(input("Enter your Subject 1 Marks : "))
# mark2 = int(input("Enter your Subject 2 Marks : "))
# mark3 = int(input("Enter your Subject 3 Marks : "))

# total_perc = ((mark1 + mark2 + mark3)/300) * 100

# if(total_perc>= 40):
#     if(mark1 < 33 or mark2 < 33 or mark3 < 33):
#         print("Failed because one of the subject has less that 33%!!")
#     else:
#         print("Pass!", total_perc)
# else:
#     print("Failed because total Percentage is below 40%!")

# Q2. WAP to check if a name is present in a list or not
nameList = ["Shashank", "Rohit", "Pankaj", "Ashish", "Shobhit", "Mayank"]
name = input("Enter a name : ")
if name in nameList:
    print(f"{name} is present in the list!")
else:
    print(f"{name} is not present in the list!")