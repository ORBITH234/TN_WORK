# try / except blocks are specifically designed to catch runtime exceptions caused by 
# operations that can fail (such as type conversions like float(), arithmetic operations 
# like dividing by zero, or looking up keys in a dictionary). 
# Simple assignments or returns do not throw value errors.

# # Write a function called `solution` that safely converts a value to a number and doubles it.

# If the value can be converted to a number, return the doubled value rounded to 2 decimal places.

# If the value cannot be converted to a number, return this exact string:

# Invalid number

# Rules:
# - Use `float()` inside a `try` block.
# - Use `except ValueError` to catch bad input.
# - Return "Invalid number" for bad input.
# - Do not print.
# - Do not ask for input.

# This challenge matches the Day 2 safe parsing idea: ask, attempt to convert, handle failure, and continue without crashing.


def solution(value):
    try:
        num = float(value)
        num = num * 2
        return (round(num,2))
    except ValueError:
        return ("Invalid number")
