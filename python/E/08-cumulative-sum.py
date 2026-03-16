numbers = [1, 2, 3, 4, 5]
cumulative_sum = []
running_total = 0

for num in numbers:
    running_total += num
    cumulative_sum.append(running_total)

print("Original list:", numbers)
print("Cumulative sum list:", cumulative_sum)

"""
Original list: [1, 2, 3, 4, 5]
Cumulative sum list: [1, 3, 6, 10, 15]
"""
