values = (1, 2, 2, 3, 4, 4, 5, 1)
unique_list = []

for value in values:
    if value not in unique_list:
        unique_list.append(value)

print("Original tuple:", values)
print("List after removing duplicates:", unique_list)

"""
Original tuple: (1, 2, 2, 3, 4, 4, 5, 1)
List after removing duplicates: [1, 2, 3, 4, 5]
"""
