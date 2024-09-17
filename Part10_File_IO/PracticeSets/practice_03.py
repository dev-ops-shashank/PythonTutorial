# WAP to replace word "Donkey" with "######" in a file.

def replaceWord(word_to_replace,word):
    with(open("./Part10_File_IO/PracticeSets/file.txt","r+") as f):
        f.seek(0)
        data = f.read()

        # Create variations of the word to replace
        variations = [
            word_to_replace.lower(),
            word_to_replace.upper(),
            word_to_replace.capitalize()
        ]

        # Replace each variation
        for variation in variations:
            data = data.replace(variation, word * len(variation))

        f.seek(0)
        f.write(data)
        f.truncate()

str1 = input("Enter word that you need to censored : ")
replaceWord(str1,"#")
