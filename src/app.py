from os import path, system
import sys

if path.dirname(path.abspath("./giada-speech-synthesis")) not in sys.path:
    sys.path.append(path.dirname(path.abspath("./giada-speech-synthesis")))
    system("cls")

from resources import *

def main() -> None:
    system("cls")
    user = input("What action would you like to execute?\n1. Add typos to your typo file\n2. View your typo file\n3. Clear your typo file\n4. Correct your text\n5. Exit the program\n-> ")
    if user == "1":
        commands.add(location)
        main()
    elif user == "2":
        commands.view(location)
        main()
    elif user == "3":
        commands.clear(location)
        main()
    elif user == "4":
        commands.correct()
        main()
    elif user == "5":
        system("cls")
    else:
        system("cls")
        main()



if __name__ == "__main__":
    location = commands.fileFinder()
    main()