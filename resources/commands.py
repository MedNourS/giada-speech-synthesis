from pathlib import Path
from resources import constants
import nltk
from nltk.corpus import words
import os



def fileFinder() -> str:
    try:
        file = str(input("Please insert the name of the text file: "))
        if ".txt" not in file:
            file += ".txt"
        return file
    except:
        return None


def convertFileToPath(file:str) -> str:
    return Path(f"resources/text_files/{file}").resolve()


def add() -> None:
    file = fileFinder()
    os.system("cls")
    file = convertFileToPath(file)
    with open(file, "a") as appender:
        changes = input("What changes would you like to make to the file?\n-> ").split("~")
        for i in changes:
            if i == "":
                pass
            else:
                appender.write(f"\n{i}")


def makeDictionary() -> None:
    file = fileFinder()
    file = convertFileToPath(file)

    with open(file, "w") as writer:
        for i in set(words.words()):
            writer.write(f"\n{i}")


def clear() -> None:
    file = fileFinder()
    file = convertFileToPath(file)
    os.system("cls")
    open(file, "w").close()
    print(f"{file} cleared")
    input()


def delete() -> None:
    file = fileFinder()
    file = convertFileToPath(file)
    os.system("cls")
    if os.path.exists("file"):
        os.remove(file)
        print(f"{file} deleted")
        input()
    else:
        print(f"{file} was not found")
        input()


def view() -> None:
    file = fileFinder()
    file = convertFileToPath(file)
    os.system("cls")
    try:
        with open(file, "r") as reader:
            tmp = []
            for i in reader.readlines():
                tmp.append(i)
            for i in range(len(tmp)):
                print(f"{i+1}. {tmp[i]}")
            input()
    except:
        print(f"{file} was not found")
        input()


def correct() -> None:
    os.system("cls")
    en_dictionary = set(words.words())
    text = input("What word would you like to be corrected?\n-> ")
    combos = []
    candidates = []
    differences = []
    combined = []
    sorted_candidates = []
    os.system("cls")
    method = input("What method would you like to use to correct your word?\n1. Fast incomplete search\n2. Slow complete search\n-> ")
    if method == "1":
        for i in text.lower():
            combos.append(constants.keyboard_dict[i])
    elif method == "2":
        for i in text.lower():
            combos.append(constants.keyboard_dict2[i])
    else:
        return correct()
    os.system("cls")
    print(combos)
    for i in generateCombosFromList(combos):
        if "".join(i).lower() in en_dictionary:
            candidates.append("".join(i))
        else:
            pass
    for candidate in candidates:
        differences.append(sum(1 for a, b in zip(candidate, [x for x in text]) if a != b))

    combined = [list(item) for item in zip(candidates, differences)]
    sorted_candidates = sorted([list(item) for item in zip(candidates, differences)], key=lambda i: i[1])
    print(sorted_candidates)
    input()
    input()


def generateCombosFromList(lists):
    if not lists:
        return [[]]
    first_list = lists[0]
    rest_lists = lists[1:]
    combinations = []
    for item in first_list:
        for combination in generateCombosFromList(rest_lists):
            combinations.append([item] + combination)
    return combinations