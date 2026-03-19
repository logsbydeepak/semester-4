numbers = (15, 3, 27, 9, 42, 6, 18)
k = 2

sorted_numbers = sorted(numbers)
minimum_k = tuple(sorted_numbers[:k])
maximum_k = tuple(sorted_numbers[-k:])

print("Tuple:", numbers)
print(f"Minimum {k} elements:", minimum_k)
print(f"Maximum {k} elements:", maximum_k)

"""
Tuple: (15, 3, 27, 9, 42, 6, 18)
Minimum 2 elements: (3, 6)
Maximum 2 elements: (27, 42)
"""
