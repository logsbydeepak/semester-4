n = int(input("Enter number of terms: "))

a = 0
b = 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

"""
Enter number of terms: 10
0 1 1 2 3 5 8 13 21 34
"""

"""
# another way using recursion

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
"""
