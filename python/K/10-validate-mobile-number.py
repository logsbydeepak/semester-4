import re

n = input("Enter mobile number: ")

if re.fullmatch(r"\d{10}", n):
    print("Valid")
else:
    print("Invalid")

"""
Enter mobile number: 9876543210
Valid
"""
