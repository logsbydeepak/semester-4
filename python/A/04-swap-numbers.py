a = 10
b = 20
print(f"Before a = {a}, b = {b}")
a, b = b, a
print(f"After a = {a}, b = {b}")

"""
Before a = 10, b = 20
After a = 20, b = 10
"""
