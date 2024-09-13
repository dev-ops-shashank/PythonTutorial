# Problem 1: Write a program to print 4 famous qoutes of your choice using a single print()
print('''1) Everything happening around me is very random. I am enjoying the phase, as the journey is far more enjoyable than the destination.
2) My mother always used to say: The older you get, the better you get, unless you’re a banana.
3) To be successful, you have to fall in love with your work
4) Always remember that you are absolutely unique. Just like everyone else.''')

# Problem 2: Install an external module and use it to perform operation of your interest
# I'm using pyttsx module that convert text to speech. For this, I'm installing the module using "pip install pyttsx3"
import pyttsx3
engine = pyttsx3.init()
engine.say('''1) Everything happening around me is very random. I am enjoying the phase, as the journey is far more enjoyable than the destination.
2) My mother always used to say: The older you get, the better you get, unless you’re a banana.
3) To be successful, you have to fall in love with your work
4) Always remember that you are absolutely unique. Just like everyone else.''')
engine.runAndWait()