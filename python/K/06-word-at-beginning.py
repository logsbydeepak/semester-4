import re

s = input("Enter a string: ")
m = re.match(r"\w+", s)

if m:
    print("Word:", m.group())
else:
    print("No match")

"""
Enter a string: Python is easy
Word: Python
"""
