numbers = [1, 2, 3, 4, 5]
number_cube_tuples = []

for num in numbers:
    number_cube_tuples.append((num, num**3))

print("Original list:", numbers)
print("List of tuples (number, cube):", number_cube_tuples)

"""
Original list: [1, 2, 3, 4, 5]
List of tuples (number, cube): [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]
"""
