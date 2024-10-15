from pathlib import Path
from resources import constants
import nltk
from nltk.corpus import words
from os import system



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


def add(file:str) -> None:
    system("cls")
    file = convertFileToPath(file)
    with open(file, "a") as appender:
        changes = input("What changes would you like to make to the file?\n-> ").split("~")
        for i in changes:
            if i == "":
                pass
            else:
                appender.write(f"\n{i}")


def clear(file:str) -> None:
    system("cls")
    file = convertFileToPath(file)
    open(file, "w").close()
    print(f"{file} cleared")
    input()


def view(file:str) -> None:
    system("cls")
    file = convertFileToPath(file)
    with open(file, "r") as reader:
        tmp = []
        for i in reader.readlines():
            tmp.append(i)
        for i in range(len(tmp)):
            print(f"{i+1}. {tmp[i]}")
        input()
    print("\n")


def correct() -> None:
    system("cls")
    en_dictionary = set(words.words())
    text = input("What word would you like to be corrected?\n-> ")
    combos = []
    candidates = []
    differences = []
    combined = []
    sorted_candidates = []
    system("cls")
    method = input("What method would you like to use to correct your word?\n1. Fast incomplete search\n2. Slow complete search\n-> ")
    if method == "1":
        for i in text.lower():
            combos.append(constants.keyboard_dict[i])
    elif method == "2":
        for i in text.lower():
            combos.append(constants.keyboard_dict2[i])
    else:
        return correct()
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