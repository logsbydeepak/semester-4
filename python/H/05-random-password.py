import random


def generate_password():
    length = random.randint(7, 10)
    password = ""
    for _ in range(length):
        password += chr(random.randint(33, 126))
    return password


print("Generated password:", generate_password())

"""
Generated password: aB#9@xP
"""
