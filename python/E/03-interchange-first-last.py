numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

if len(numbers) >= 2:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("List after interchanging first and last elements:", numbers)

"""
Original list: [10, 20, 30, 40, 50]
List after interchanging first and last elements: [50, 20, 30, 40, 10]
"""
