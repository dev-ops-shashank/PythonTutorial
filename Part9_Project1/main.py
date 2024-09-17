'''
1 for Snake
-1 for Water
0 for Gun
'''
import random
# generating random number for computer
compChoice = random.choice([-1, 0, 1])

print("\n!! Welcome to Snake-Water-Gun !!\n")
print('''Following are the rules of the game:
    * Snake vs. Water: Snake drinks the water hence wins.
    * Water vs. Gun: The gun will drown in water, hence a point for water
    * Gun vs. Snake: Gun will kill the snake and win.''')

yourChoice = input("Enter your choice ('s' for Snake, 'w' for Water, 'g' for Gun) : ").lower()
yourDict = {'s' : 1 , 'w' : -1, 'g' : 0}
reversedDict = {1 : 'Snake', -1 : 'Water', 0 : 'Gun'}

you = yourDict[yourChoice]

print(f"Your Choice : {reversedDict[you]}\nComputer's Choice : {reversedDict[compChoice]}")

if(you == compChoice):
    print("Its a Draw!")
else:
    if((compChoice==-1 and you==1) or (compChoice==1 and you==0) or (compChoice==0 and you==-1)):
        print("You Win!")
    elif((compChoice==-1 and you==0) or (compChoice==0 and you==1) or (compChoice==1 and you==-1)):
        print("You Lose!")
    else:
        print("!!!!!Something went wrong!!!!!")

# You can optimise the conditions according to your need as long as you are getting the desired Output