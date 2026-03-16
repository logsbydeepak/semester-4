numbers = [10, 20, 30, 40, 50]
old_value = 30
new_value = 35

print("Original list:", numbers)

if old_value in numbers:
    index = numbers.index(old_value)
    numbers[index] = new_value
    print(f"Replaced {old_value} with {new_value}")
else:
    print(f"{old_value} not found in the list")

print("Updated list:", numbers)

"""
Original list: [10, 20, 30, 40, 50]
Replaced 30 with 35
Updated list: [10, 20, 35, 40, 50]
"""
