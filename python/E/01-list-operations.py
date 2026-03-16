numbers = [10, 20, 30, 40]
print("Original list:", numbers)

numbers.append(50)
print("After append(50):", numbers)

numbers.insert(1, 15)
print("After insert(1, 15):", numbers)

numbers.remove(30)
print("After remove(30):", numbers)

popped_element = numbers.pop()
print("After pop():", numbers)
print("Popped element:", popped_element)

print("Slice [1:4]:", numbers[1:4])
print("Length of list:", len(numbers))

"""
Original list: [10, 20, 30, 40]
After append(50): [10, 20, 30, 40, 50]
After insert(1, 15): [10, 15, 20, 30, 40, 50]
After remove(30): [10, 15, 20, 40, 50]
After pop(): [10, 15, 20, 40]
Popped element: 50
Slice [1:4]: [15, 20, 40]
Length of list: 4
"""
