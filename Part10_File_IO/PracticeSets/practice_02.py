# Q) The game() function in a program lets a user to play a game and returns the score as an integer. 
# You need to read a file 'HiScore.txt' which is either blank or contains the previous Hi-Score. 
# You need to write a program to update the Hi-Score whenver the game() breaks the Hi-Score

def game():
# game is to count no. of times 'a' appears in the string given by user.
# and returns the count as a score
    str = input("Enter a Statement : ").lower()
    score = str.count('a')
    print("Your Score : ", score)
    return score

hiscore = game()

with(open("./Part10_File_IO/PracticeSets/HiScore.txt","r+") as f):
    data = f.read()
    if data == "":
        if(hiscore==0):
            f.write("0")
        else:
            f.write(str(hiscore))
    elif int(data) < hiscore:
        f.seek(0)
        f.write(str(hiscore))
    f.seek(0)
    data = f.read()
    print("High Score is : ", data)
