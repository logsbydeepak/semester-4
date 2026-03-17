numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

print("List after squaring each element:", numbers)

"""
Original list: [1, 2, 3, 4, 5]
List after squaring each element: [1, 4, 9, 16, 25]
"""
