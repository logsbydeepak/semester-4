from functools import reduce

numbers = [10, 20, 30, 40, 50]
total = reduce(lambda x, y: x + y, numbers)

print("List:", numbers)
print("Sum of elements:", total)

"""
List: [10, 20, 30, 40, 50]
Sum of elements: 150
"""
