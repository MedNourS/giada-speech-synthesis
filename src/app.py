from os import path, system
import sys

if path.dirname(path.abspath("./giada-speech-synthesis")) not in sys.path:
    sys.path.append(path.dirname(path.abspath("./giada-speech-synthesis")))
    system("cls")

from resources import *

def main() -> None:
    system("cls")
    user = input("What action would you like to execute?\n1. Add elements to your text file\n2. View your text file\n3. Clear your text file\n4. Delete your text file\n5. Correct a word\n6. Make a dictionary file\n7. Exit the program\n-> ")
    if user == "1":
        commands.add()
        main()
    elif user == "2":
        commands.view()
        main()
    elif user == "3":
        commands.clear()
        main()
    elif user == "4":
        commands.delete()
        main()
    elif user == "5":
        commands.correct()
    elif user == "6":
        commands.makeDictionary()
        main()
    elif user == "7":
        system("cls")
    else:
        system("cls")
        main()



if __name__ == "__main__":
    main()