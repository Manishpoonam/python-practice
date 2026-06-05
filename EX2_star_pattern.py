#write a Python program that generates a triangle star pattern based on two user inputs: 
#an integer (representing the number of rows) and a binary integer (0 or 1).
#The program needs to do the following:
# Accept an integer for the row count (e.g., 5).
# Accept 0 or 1 as input and typecast it into a proper Python boolean (False or True).
# If the boolean is True, print an ascending pattern:
# *
# **
# ***
# ****
# *****
# If the boolean is False, print a descending pattern:
# Plaintext
# *****
# ****
# ***
# **
# *

#----------------------------------------------------------------------------------------------------


n = int(input("Enter the number f rows: "))
boll_val = int(input("Enter 1 for True and 0 for False: "))

is_ascending = bool(boll_val)

if is_ascending:
    for i in range(1, n + 1):
        print("*" * i)