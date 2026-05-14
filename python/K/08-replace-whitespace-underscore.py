import re

s = input("Enter a string: ")

u = re.sub(r"\s+", "_", s)
t = re.sub(r"_", " ", s)

print("Space to underscore:", u)
print("Underscore to space:", t)

"""
Enter a string: hello_world test
Space to underscore: hello_world_test
Underscore to space: hello world test
"""
