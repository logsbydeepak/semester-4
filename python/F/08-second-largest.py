numbers = (10, 20, 4, 45, 99, 99, 45)
unique_numbers = sorted(set(numbers))

print("Tuple:", numbers)

if len(unique_numbers) < 2:
    print("Second largest element does not exist")
else:
    second_largest = unique_numbers[-2]
    print("Second largest element:", second_largest)

"""
Tuple: (10, 20, 4, 45, 99, 99, 45)
Second largest element: 45
"""
