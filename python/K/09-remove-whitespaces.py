import re

s = input("Enter a string: ")

print(re.sub(r"\s+", "", s))

"""
Enter a string: p y t h o n
python
"""
