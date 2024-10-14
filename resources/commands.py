from pathlib import Path


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
    print("\n")
    file = convertFileToPath(file)
    with open(file, "a") as appender:
        changes = input("What changes would you like to make to the file? ").split("~")
        for i in changes:
            if i == "":
                pass
            else:
                appender.write(f"\n{i}")
    print("\n")


def clear(file:str) -> None:
    print("\n")
    file = convertFileToPath(file)
    open(file, "w").close()
    print("\n")


def view(file:str) -> None:
    print("\n")
    file = convertFileToPath(file)
    with open(file, "r") as reader:
        tmp = []
        for i in reader.readlines():
            tmp.append(i)
        for i in range(len(tmp)):
            print(f"{i+1}. {tmp[i]}")
        input()
    print("\n")


#def engaged() -> bool:
#    print("\n")
#    user = input("Do you require another operation? ")
#    print("\n")
#
#    if user.lower() == "yes" or user.lower() == "y":
#        return True
#    else:
#        return False