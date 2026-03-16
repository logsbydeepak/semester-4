numbers = []

while True:
    num = int(input("Enter an integer (0 to stop): "))
    if num == 0:
        break
    numbers.append(num)

numbers.sort()

print("Values from smallest to largest:")
for value in numbers:
    print(value)

"""
Enter an integer (0 to stop): 5
Enter an integer (0 to stop): 2
Enter an integer (0 to stop): 9
Enter an integer (0 to stop): 1
Enter an integer (0 to stop): 0
Values from smallest to largest:
1
2
5
9
"""
