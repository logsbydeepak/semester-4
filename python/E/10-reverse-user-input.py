numbers = []

while True:
    num = int(input("Enter an integer (0 to stop): "))
    if num == 0:
        break
    numbers.append(num)

print("Values in reverse order:")
for value in reversed(numbers):
    print(value)

"""
Enter an integer (0 to stop): 10
Enter an integer (0 to stop): 20
Enter an integer (0 to stop): 30
Enter an integer (0 to stop): 0
Values in reverse order:
30
20
10
"""
