import re

s = input("Enter a string: ")

if re.fullmatch(r"\w+", s):
    print("Valid")
else:
    print("Invalid")

"""
Enter a string: Abc_123
Valid
"""
