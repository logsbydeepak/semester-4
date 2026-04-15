def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


n = int(input("Enter a number: "))

print("Factorial:", fact(n))

"""
Enter a number: 5
Factorial: 120
"""
