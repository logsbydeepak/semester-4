import re

s = input("Enter a string: ")

if re.search(r"cat|dog|fox", s):
    print("Found")
else:
    print("Not found")

"""
Enter a string: The fox is clever
Found
"""
