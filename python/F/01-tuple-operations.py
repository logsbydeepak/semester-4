numbers = (10, 20, 30, 40, 50)
print("Original tuple:", numbers)

print("Length of tuple:", len(numbers))
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Slice [1:4]:", numbers[1:4])

count_20 = numbers.count(20)
index_40 = numbers.index(40)
print("Count of 20:", count_20)
print("Index of 40:", index_40)

new_tuple = numbers + (60, 70)
print("After concatenation:", new_tuple)

"""
Original tuple: (10, 20, 30, 40, 50)
Length of tuple: 5
First element: 10
Last element: 50
Slice [1:4]: (20, 30, 40)
Count of 20: 1
Index of 40: 3
After concatenation: (10, 20, 30, 40, 50, 60, 70)
"""
