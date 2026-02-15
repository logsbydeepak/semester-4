num = int(input("Enter year: "))

if ((num % 4 == 0) and (num % 100 != 0)) or (num % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

"""
Enter year: 2000
Leap year
"""
