# Q) WAP to prinf following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# for i in range(0,5):
#     s=""
#     for i in range(0, i+1):
#         s=s+"* "
#     print(s)

# Q) WAP to prinf following pattern
#     *
#    ***
#   *****
# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#         print(" " * (n-i), end="")
#         print("*" * (2*i-1), end="")
#         print("")

# Q) WAP to prinf following pattern
# * * *
# *   *
# * * *
# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n, end="")
#     else:
#         print("*", end="")
#         print(" "*(n-2), end="")
#         print("*", end="")
#     print("")

