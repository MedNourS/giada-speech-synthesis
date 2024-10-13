def fileFinder() -> str:
    try:
        file = str(input("Please insert the name of the text file containing the typos: "))
        if ".txt" not in file:
            file += ".txt"
        return file
    except:
        return None


def main() -> bool:
    user = input("What action would you like to execute?\n1. Add typos to your typo file\n2. Clear your typo file\n-> ")
    if user == "1":
        add(location)
    elif user == "2":
        clear(location)


def add(file:str):
    changes = input("What changes would you like to make to the file? ").split(" ")
    with open(file, "a") as appender:
        for i in changes:
            if i == "":
                pass
            else:
                appender.write(f"\n{i}")


def clear(file:str):
    open(file, "w").close()


def engaged() -> bool:
    user = input("Do you require another operation? ")
    if user.lower() == "yes" or "y":
        return True
    else:
        return False



if __name__ == "__main__":
    location = fileFinder()
    main()
    while(True):
        if engaged() == True:
            print("\n")
            main()
        else:
            break