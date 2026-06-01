#---------------File Handling-------------
#It has several functions for creating, reading, updating, and deleting files.

        # "r" - Read - Default value. Opens a file for reading, error if the file does not exist

        # "a" - Append - Opens a file for appending, creates the file if it does not exist

        # "w" - Write - Opens a file for writing, creates the file if it does not exist

        # "x" - Create - Creates the specified file, returns an error if the file exists

        # In addition you can specify if the file should be handled as binary or text mode

        # "t" - Text - Default value. Text mode

        # "b" - Binary - Binary mode (e.g. images)


# Open a File on the Server---------
f = open("demo.txt")
print(f.read())
f.close #you must write a close statement in order to close the file

with open ("demo.txt") as f: #You can also use the with statement when opening a file
    print(f.read())

#Read Lines-----
with open("demo.txt") as f:
    print(f.readline())
    print(f.readline()) #By calling readline() two times, you can read the two first lines

#Write to an Existing File-----------
        # "a" - Append - will append to the end of the file
        # "w" - Write - will overwrite any existing content
with open("demo.txt", "a") as f:
    f.write("By the way, bye bye!")
with open("demo.txt") as f: #open and read the file after the appending:
    print(f.read())

#Overwrite Existing Content--------
with open("demo.txt", "w") as f:
    f.write("Opps all override")
with open("demo.txt")as f:
    print(f.read())

#To create a new file------
f = open("newfile.txt", "x") #If the file already exists, an error will be raised.
