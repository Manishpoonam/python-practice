# ---------Strings----------

print("Hello")
print('Hello')


# Quotes Inside Quotes ---
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


# Assign String to a Variable --
a = "Hello"
print(a)


# Multiline Strings ---
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)


#Strings are Arrays ---
a = "Hello, World!"
print(a[1])


# Looping Through a String ---
for x in 'Banana':
    print(x)

#String Length ---
c = "Hello, World!"
print(len(c))


#Check String ---
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes 'free' is present in text")
else:
    print("No, it is not present")

#Slicing Strings ----

#Slicing
b = "Hello, World!"
print(b[0:4])    #Get the characters from position 2 to position 5 (not included)

#Slice From the Start
print(b[:6])

#Slice To the End
print(b[2:])

#Negative Indexing
print(b[-5:-2])

#--------------------This all are methods---------

#Lower Case
print(a.lower())

#Upper Case
print(a.upper())

#Remove Whitespace
a=" Hello i am Manish "
print(a.strip())     #This method removes any whitespace from the beginning or the end

#Replace String
print(a.replace("M", "V"))

#Split String
a = "Hello world i am Manish"  #method returns a list where the text between the specified separator becomes the list items.
print(a.split(","))            #method splits the string into substrings if it finds instances of the separator.

#String Format ---
#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

# age = 36
#This will produce an error:
# txt = "My name is John, I am " + age
# print(txt)

#F-Strings
age = 36
txt = f"My name is Manish, I am {age}"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)





#LIST OF SOME METHODS -----

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values from a dictionary in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning



