import json
from difflib import get_close_matches

# This is a dictionary file
data = json.load(open("data.json"))

a = "d"
while a == "d":
    def translate(word):
        word = word.lower()
        if word in data:
            return data[word]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif len(get_close_matches(word, data.keys())) > 0 :
            print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
            decide = input("Press Y for yes, press N for no ")
            if decide.upper() == "Y":
                return data[get_close_matches(word, data.keys())[0]]
            elif decide.upper() == "N":
                print("The word doesn't exist, please check it again")
            else:
                print("You have entered wrong input, please enter Y or N")
        else:
            print("The word doesn't exist, please check it again.")

    word = input("Enter the word you want to search: ")
    output = translate(word)
    a = 1
    if type(output) == list:
        for item in output:
            print(a , ".", item)
            a += 1
    else :
        print(output)

    a = input("\n\nIf you want to close the dictionary press any key\n" +
            "If you want to check for another word press 'd' to restart ").lower()






# You are going to upload a json file and these files can be found in internet
