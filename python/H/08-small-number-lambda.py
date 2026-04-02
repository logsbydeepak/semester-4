num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

smallest = (lambda a, b: a if a < b else b)(num1, num2)
print("Smaller number is:", smallest)

"""
Enter first number: 15
Enter second number: 9
Smaller number is: 9
"""
