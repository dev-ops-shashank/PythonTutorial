name = "Guido_van_Rossum"
# G u i d o _ v a n _ R  o  s  s  u  m
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 || -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(name)
# string slicing: The general form of slicing is string[start:end:step], where start and end are the indices, and step/skip is optional.
print(name[0:6])        # Slicing the string
print(name[-7:-1])      # negative slicing of the string
print(name[1:7])

print(name[:8])         # if colon's left is blank, its 0. name[:8] is same as name[0:8]
print(name[5:])         # if colon's right is blank, its len-1 name[5:] is same as name[5:16]

print(name[4:1])        # will not give any output. When the start index is 
# greater than the end index in a slice, and there's no negative step provided, Python returns an empty string.
# but if we add a negative step in this slicing, it will give an output in reverse
print(name[14:1:-1])     # Output in reverse
print(name[14:1:-2])     # Output in reverse
print(name[14:1:-3])     # Output in reverse
# now question arive, why use '-1' as step? The choice of step affects how many characters are skipped.
# -1 mean no skipping any character, -2 means if you start from 8 and moving towards 1, then output charater on 8(-2)6(-2)4(-2)2(-2)0
# same goes with -3, -4 etc steps.
# We rarely use negative index
print(name[14:1:-2])     # Output in reverse
print(name[-2:1:-2])     # -2 is same as 14

