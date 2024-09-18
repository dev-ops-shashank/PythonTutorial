# WAP to open 3 files file1.txt, file2.txt, file3.txt, if any file is not present, a message
# must be printed, without exiting the code, prompting the same 

try:
    print("Opening file1.txt......")
    with(open("./Part12_AdvancePython1/PracticeSets/file1.txt") as f1):
        print("Successfully opened File1. Here is its content:")
        print(f1.read())
except FileNotFoundError:
    print("File not present!")
try:
    print("Opening file2.txt......")
    with(open("./Part12_AdvancePython1/PracticeSets/file2.txt") as f2):
        print("Successfully opened File2. Here is its content:")
        print(f2.read())
except FileNotFoundError:
    print("File not present!")
try:
    print("Opening file3.txt......")
    with(open("./Part12_AdvancePython1/PracticeSets/file3.txt") as f3):
        print("Successfully opened File3. Here is its content:")
        print(f3.read())
except FileNotFoundError:
    print("File not present!")

print("Thank you!!")

# FileNotFoundError