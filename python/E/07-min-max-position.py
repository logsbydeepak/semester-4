numbers = [25, 10, 45, 5, 30]
minimum = min(numbers)
maximum = max(numbers)

min_position = numbers.index(minimum)
max_position = numbers.index(maximum)

print("List:", numbers)
print(f"Minimum element {minimum} is at position {min_position}")
print(f"Maximum element {maximum} is at position {max_position}")

"""
List: [25, 10, 45, 5, 30]
Minimum element 5 is at position 3
Maximum element 45 is at position 2
"""
