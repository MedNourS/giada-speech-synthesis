def fileFinder() -> str:
    try:
        file = str(input("Please insert the name of the text file containing the typos: "))
        if ".txt" not in file:
            file += ".txt"
        return file
    except:
        return None


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


def main():
    location = fileFinder()
    clear(location)
    add(location)



if __name__ == "__main__":
    main()