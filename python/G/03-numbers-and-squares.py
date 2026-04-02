n = int(input("Enter N: "))
squares = {}

for i in range(1, n + 1):
    squares[i] = i * i

print("Dictionary of numbers and squares:", squares)

"""
Enter N: 5
Dictionary of numbers and squares: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
