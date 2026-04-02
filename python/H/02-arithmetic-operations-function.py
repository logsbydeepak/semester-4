def arithmetic_operations(a, b):
    return a + b, a - b, a * b, a / b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

addition, subtraction, multiplication, division = arithmetic_operations(num1, num2)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

"""
Enter first number: 15
Enter second number: 4
Addition: 19
Subtraction: 11
Multiplication: 60
Division: 3.75
"""
