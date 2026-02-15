num1 = int(input("Enter 1'st number: "))
num2 = int(input("Enter 2'nd number: "))
num3 = int(input("Enter 3'rd number: "))

if num1 >= num2 and num1 >= num3:
    print(f"1's number is largest: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"2's number is largest: {num2}")
else:
    print(f"3's number is largest: {num3}")

"""
Enter 1'st number: 1
Enter 2'nd number: 2
Enter 3'rd number: 3
3's number is largest: 3
"""
