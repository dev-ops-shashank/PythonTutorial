f = open("./Part10_File_IO/file2.txt","w+")
# This will create a new file opened with write access
f.write('''
OS manages computer resources efficiently.
Windows, macOS, Linux are popular OS choices.
OS provides interface between hardware and user.
Multitasking is a key feature of modern OS.
File systems organize data storage in OS.''')
f.seek(0)
fileContent = f.read()
print(fileContent)

print("===============")
f.seek(0)                                       # Move the file pointer to the beginning
readbylines = f.readline()
# Read first 3 lines of the file
for i in range(0,3):
    print(f.readline(), end="")
f.seek(0)
f.close()

##################################################
# using with() we can be stressfree with close() usage. 
# with() give us ability to work with files without explicitly mentioning the close(). Here's how:

'''with(open("./Part10_File_IO/file2.txt","r+") as f):
# w+ will create a new file, if the file doesn't exists, if exist, it will delete all its content
# r+ will open the file with write option also. If file doesn't exist, it will give error.
    print(f.read())'''