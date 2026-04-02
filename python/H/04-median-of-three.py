def median_of_three(a, b, c):
    values = [a, b, c]
    values.sort()
    return values[1]


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

median = median_of_three(num1, num2, num3)
print("Median value:", median)

"""
Enter first number: 5
Enter second number: 9
Enter third number: 7
Median value: 7
"""
