###################################################################################################
# GB | Learning Python Fundamentals
# In this file, I will add fundamental Python concepts and examples for different use cases
# as I learn how to use the language.
#
# IMPORTANT NOTES:
#   1. Everything in Python is an object.
#   2. Objects have methods that can be accessed with dot notation (.) after the variable name.
#   3. Working with numbers using the math module: https://docs.python.org/3/library/math.html
###################################################################################################

import math

#######################################
# Working with strings and substrings
#######################################

course = "python programming"
print(f"\nWorking with the course variable: {course}\n")

# len: returns the length of the string => 18
print(f"len: {len(course)}")

# First letter => p
print(f"first letter: {course[0]}")

# Last letter => g
print(f"last letter: {course[-1]}")

# Substring from index 0 to 3 (index 3 is not included) => pyt
print(f"sub-string 0:3: {course[0:3]}")

# Substring from index 0 to the end of the string => python programming
print(f"sub-string 0:: {course[0:]}")

# When the starting index is omitted, Python uses 0 by default => pyt
print(f"sub-string :3: {course[:3]}")

# When both indexes are omitted, Python returns the entire string
print(f"sub-string :: {course[:]}")

# Escape sequences in Python:
# \"
# \'
# \\
# \n

first = "Gunnar"
last = "Bolanos"

# String concatenation
full_concatenation = first + " " + last
print("Concatenated string: " + full_concatenation)

# Formatting string
full_formatting = f"{first} {last}"
print("Formatting string: " + full_formatting)

testing_formatting_uses = f"{len(first)} {2 + 2}"
print(testing_formatting_uses)

#######################################
# Common string methods
#######################################

# upper: converts the entire string to uppercase
print(course.upper())

# lower: converts the entire string to lowercase
print(course.lower())

# title: capitalizes the first letter of every word
print(course.title())

# strip: removes extra whitespace from the beginning and end of a string
print(course.strip())

# find: returns the starting index of a substring; returns -1 if it is not found
print(course.find("pro"))

# replace: replaces every occurrence of the first argument with the second argument
print(course.replace("p", "j"))

# in: returns True or False depending on whether a substring exists in the string
print("pro" in course)

# not in: returns True when a substring does not exist in the string
print("swift" not in course)

#######################################
# Working with numbers
#######################################

print("\nWorking with numbers\n")
print(f"Addition 10 + 3 = {10 + 3}")
print(f"Subtraction 10 - 3 = {10 - 3}")
print(f"Multiplication 10 * 3 = {10 * 3}")
print(f"Division 10 / 3 = {10 / 3}")
print(f"Floor division 10 // 3 = {10 // 3}")
print(f"Modulo 10 % 3 = {10 % 3}")
print(f"Exponentiation 10 ** 3 = {10 ** 3}")
print(f"Round 2.9: {round(2.9)}")
print(f"Absolute value of -2.9: {abs(-2.9)}")
print(f"Ceiling of 2.2: {math.ceil(2.2)}")

#######################################
# Working with type conversion
#######################################

# input returns a string, so int converts the value before adding a number
# x = input("x: ")
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# Common falsy values in Python include an empty string, zero, and None: "", 0, None

#######################################
# Working with conditional statements
#######################################

temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

age = 22

# Full if/else statement
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
print(f"\nfull if/else: {message}")

# Conditional expression (also known as a ternary operator)
message_ternary = "Eligible" if age >= 18 else "Not eligible"
print(f"\nternary condition: {message_ternary}")

# Logical operators

high_income = False
good_credit = True
student = True

print("\nAnd operator")
if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

print("\nOr operator")
if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

print("\nNot operator")
if not student:
    print("Eligible")
else:
    print("Not eligible")

print("\nAll the operators")
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

#######################################
# Working with for loops
#######################################

# range(3) starts at 0 by default and stops before 3
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

# Start at 1 and stop before 4, avoiding the need to add 1 inside the loop
for number in range(1, 4):
    print("Attempt", number, number * ".")

# Start at 1, stop before 10, and increment by 2 on each iteration
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# Try up to three times and exit the loop early when successful
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break

# The else block runs only when the loop finishes without encountering break
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# Nested loop: run the inner loop completely for each outer-loop iteration
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Keep requesting input until the user enters "quit" (case-insensitive)
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
