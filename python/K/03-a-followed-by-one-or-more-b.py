import re

s = input("Enter a string: ")

if re.fullmatch(r"ab+", s):
    print("Matched")
else:
    print("Not matched")

"""
Enter a string: abbb
Matched
"""
