marks = int(input("Enter your marks: "))

if marks >= 80 and marks <= 100:
    print("Excellent")
elif marks >= 65 and marks < 80:
    print("Good")
elif marks >= 50 and marks < 65:
    print("Pass")
elif marks >= 0 and marks < 50:
    print("Fail")
else:
    print("Invalid marks")

"""
Enter your marks: 45
Fail
"""
