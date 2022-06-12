# ----------------------- PYTHON DATA TYPES ----------------------------- #
# Python supports two types of numbers - Integers and Floats (also support complex numbers)
myInt, myFloat, myFloatClass = 7, 7.0, float(7)
print("Integer : ", myInt, ' , Float : ', myFloat, ' , Float with float class : ', myFloatClass)

# Strings are defined either with a single quote or a double quotes.
myString = "Hello, World"
print("String : ", myString)

# Lists are very similar to arrays. They can contain any type of variable
myList = [1, 2, 3, "Hello World", float(34)]
# without iteration
print(myList)

# with iteration
for x in myList:
    print(x)

# ----------------------- PYTHON BASIC OPERATORS ----------------------------- #

print(5 + 7)  # Addition of two numbers
print("HELOO" + " WROLD")  # Addition of two strings
print(5 * 5)  # multiply
print("HELLO " * 5)  # creating repetition of string using multiple operator
print(10 / 5)  # Divide
print([1, 2, 3] + [4, 5, 6])  # addition of lists
print([1, 2, 3] * 3)  # creating list with sequence using multiple

# ----------------------- PYTHON STRING FORMATTING ----------------------------- #

# % is used to format a set of variables enclosed in a "tuple" (a fixed size list),
# together with a format string, which contains normal text together with
# "argument specifiers", special symbols like "%s" and "%d"
# %s - String (or any object with a string representation, like numbers)

# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

name, age = 'John', 23
print("Hello, %s" % name)
print("%s is %d years old." % (name, age))  # should follow order in the tuple
print("A list: %s" % myList)

# ----------------------- PYTHON STRING OPERATIONS ----------------------------- #
string = "Hello world!"
print(len(string))  # calculate length of a string
print(string.index("o"))  # gets the index of the character
print(string.count("l"))  # gets the no of occurrences of the character in a string
print(string[3:7])  # prints a slice of the string, starting at index 3, and ending at index 6
print(string[
      3:7:2])  # prints the characters of string from 3 to 7 skipping 2 characters. This is extended slice syntax. The general form is [start:stop:step].
print(string[::-1])  # syntax to easily reverse a string
print(string.upper())  # all letters converted to uppercase and lowercase, respectively
print(string.lower())  # all letters converted to uppercase and lowercase, respectively
print(string.startswith("Hello"))  # whether the string starts with something or ends with something, respectively.
print(string.endswith("asdfasdfasdf"))  # whether the string starts with something or ends with something, respectively.
print(string.split(" "))  # splits the string into a bunch of strings grouped together in a list.

# ----------------------- PYTHON CONDITIONS ----------------------------- #
x = 2
print(x == 2)  # prints out True
print(x == 3)  # prints out False
print(x < 3)  # prints out True

# "and" and "or" boolean operators allow building complex boolean expressions
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# "in" operator could be used to check if a specified object exists within an iterable object container, such as a list
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

# the "is" operator does not match the values of the variables, but the instances themselves.
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # Prints out False

# "not" before a boolean expression inverts it
print(not False)  # Prints out True
print((not False) == False)  # Prints out False
