import re

s = input("Enter a string: ")
r = re.findall(r"[A-Z][a-z]+", s)

print("Matches:", r)

"""
Enter a string: Hello I am From India
Matches: ['Hello', 'From', 'India']
"""
