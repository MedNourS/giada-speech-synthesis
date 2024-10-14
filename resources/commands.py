from pathlib import Path
from resources import constants
import nltk
from nltk.corpus import words



def fileFinder() -> str:
    try:
        file = str(input("Please insert the name of the text file containing the typos: "))
        if ".txt" not in file:
            file += ".txt"
        return file
    except:
        return None


def convertFileToPath(file:str) -> str:
    return Path(f"resources/text_files/{file}").resolve()


def add(file:str) -> None:
    file = convertFileToPath(file)
    with open(file, "a") as appender:
        changes = input("What changes would you like to make to the file? ").split("~")
        for i in changes:
            if i == "":
                pass
            else:
                appender.write(f"\n{i}")


def clear(file:str) -> None:
    file = convertFileToPath(file)
    open(file, "w").close()


def view(file:str) -> None:
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
    en_dictionary = set(words.words())
    text = input("What text would you like to be corrected? ")
    combos = []
    candidates = []
    differences = []
    combined = []
    sorted_candidates = []
    for i in text.lower():
        combos.append(constants.keyboard_dict2[i])
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