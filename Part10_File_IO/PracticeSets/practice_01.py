# Q) WAP to read th text from a given file 'poems.txt' and find how many times word 'Star' appears

with(open("./Part10_File_IO/PracticeSets/Poems.txt","r+") as f):
    # print(f.read())
    f.seek(0)
    line = f.readline()
    count = 0
    while(line != ""):
        if("star" in line.lower()):
            count += 1
        line = f.readline()
if count>0:
    print(f"'Star' word appears {count} time in the file.")
else:
    print("'Star' word does not appear in the file.")