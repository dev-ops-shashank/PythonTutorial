# WAP to create a copy of a file 

'''with(open("./Part10_File_IO/PracticeSets/file.txt") as f1):
    data = f1.read()
with(open("./Part10_File_IO/PracticeSets/file2.txt","w+") as f2):
    f2.write(data)'''


# Now check if both files are identical or not

'''with(open("./Part10_File_IO/PracticeSets/file.txt") as f1):
    data_of_file1 = f1.read()
with(open("./Part10_File_IO/PracticeSets/file2.txt") as f2):
    data_of_file2 = f2.read()
if data_of_file1 == data_of_file2:
    print("Identical Files!")
else:
    print("Non-Identical Files!")'''

# Rename a file
'''import os
os.rename("./Part10_File_IO/PracticeSets/file2.txt","./Part10_File_IO/PracticeSets/ABC.txt")'''