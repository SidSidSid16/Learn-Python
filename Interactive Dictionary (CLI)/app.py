import json
from difflib import get_close_matches

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

data = json.load(open("dictionary_compact.json"))
print(f"{bcolors.BOLD}{bcolors.UNDERLINE}Enter 'exit()' to quit the program at any time{bcolors.ENDC}")

def app():
    word = input(f"{bcolors.HEADER}{bcolors.BOLD}Enter word: {bcolors.ENDC}")
    if word == "exit()":
        print(f"{bcolors.OKGREEN}bye bye{bcolors.ENDC}")
        exit()
    else:
        definitionOfWord(word)

def definitionOfWord(w):
    w = w.lower()
    if w in data:
        print(data[w])
        app()
    elif len(get_close_matches(w, data.keys())) > 0:
        print(f"{bcolors.FAIL}{bcolors.BOLD}The word you've entered is invalid!{bcolors.ENDC}")
        closeMatch = get_close_matches(w, data.keys())[0]
        print(f"{bcolors.WARNING}Did you mean {bcolors.OKGREEN}{bcolors.BOLD}{bcolors.UNDERLINE}%s{bcolors.ENDC}{bcolors.WARNING} instead?{bcolors.ENDC}" % (closeMatch))
        userInput = input("enter 'y()' for yes or enter another word: ")
        if userInput == 'y()':
            definitionOfWord(closeMatch)
        elif userInput == "exit()":
            print(f"{bcolors.OKGREEN}bye bye{bcolors.ENDC}")
            exit()
        else:
            definitionOfWord(userInput)
    else:
        print(f"{bcolors.FAIL}{bcolors.BOLD}The word you've entered is invalid! Please try again...{bcolors.ENDC}")
        app()


app()
