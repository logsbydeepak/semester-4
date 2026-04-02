def swap_numbers(a, b):
    return b, a


num1 = 10
num2 = 20
print(f"Before swapping: num1 = {num1}, num2 = {num2}")
num1, num2 = swap_numbers(num1, num2)
print(f"After swapping: num1 = {num1}, num2 = {num2}")

"""
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
"""
