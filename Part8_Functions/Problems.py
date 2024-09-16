# Q) WAP using function to find greatest of 3 numbers
'''
def greatest(num1, num2, num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
    
print("Find greatest of 3 numbers:")
num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))
num3 = int(input("Enter number : "))
print(f"Greatest number among these 3 numbers is : {greatest(num1,num2,num3)}")
'''

# Q) WAP to print below pattern: n=3
# ***
# **
# *
'''def pattern(n):
    if n==0:
        return
    if n>=1:
        print("*" * n)
    pattern(n-1)

num = int(input("Enter a number : "))
pattern(num)'''

# Q) WAP to remove a given word from a list and stip it from every other word at same time
'''def rem(l, word):
    n=[]
    for item in l:
        if item != word:
            n.append(item.strip(word))
    return n
l = ["Shobhit", "Shashank", "Ashish", "Mayank", "sh"] 
print(rem(l,"sh"))'''