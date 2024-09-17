f = open("./Part10_File_IO/file1.txt","r+")
# Note: you can't use f = open("*\\file.txt"), as * is not used in file system, 
# its typically used in shell commands
data = f.read()
print(data)
f.write('''
V1.1
    We Updated the content of this file.''')

# After reading or writing, the file pointer is at the end of the read/written data.
# Use file.seek(0) to move the pointer back to the beginning.
f.seek(0)
print("=============================================================================")
data=f.read()

print(data)
f.close()

########################################################
# to find the Current Working Directory:-
# import os
# print("Current Working Directory: ", os.getcwd())