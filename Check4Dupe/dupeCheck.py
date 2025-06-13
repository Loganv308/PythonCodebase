import os

DUPLICATES = []
REMOVEDFILES = []
STRINGTOCHECK = "(1)"

def main():
    path = input("List Path to search for duplicate files: ")

    print("Listing Files located in: " + path)

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if STRINGTOCHECK in filename:
                DUPLICATES.append(dirpath + "\\" + filename)

    for val in DUPLICATES:
        print(val)

    print(str(len(DUPLICATES)) + " Files in list" )

    removeYN = input("Would you like to remove these files? ")

    if(removeYN == "Y" or removeYN == "y"):

        print("Removing duplicates...")

        for file in DUPLICATES:
            print("Removing " + file)
            REMOVEDFILES.append(file)
            os.remove(file)

        print(str(len(REMOVEDFILES)) + " files have been removed")
    else:
        print("Not removing files, exiting...")

if __name__ == "__main__":
    main()
     