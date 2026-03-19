numbers = (1, 2, 3, 2, 4, 1, 2)
frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("Tuple:", numbers)
print("Frequency of elements:", frequency)

"""
Tuple: (1, 2, 3, 2, 4, 1, 2)
Frequency of elements: {1: 2, 2: 3, 3: 1, 4: 1}
"""
