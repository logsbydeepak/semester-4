def total():
    n = input("Enter a value: ")

    if n == "":
        return 0.0

    return float(n) + total()


print("Total:", total())

"""
Enter a value: 10
Enter a value: 20
Enter a value: 5.5
Enter a value:
Total: 35.5
"""
