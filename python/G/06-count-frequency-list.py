numbers = [1, 2, 2, 3, 1, 4, 2, 5, 1]
frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("List:", numbers)
print("Frequency of elements:", frequency)

"""
List: [1, 2, 2, 3, 1, 4, 2, 5, 1]
Frequency of elements: {1: 3, 2: 3, 3: 1, 4: 1, 5: 1}
"""
