def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def show(n, i=0):
    if i == n:
        return
    print(fib(i), end=" ")
    show(n, i + 1)


n = int(input("Enter number of terms: "))
show(n)

"""
Enter number of terms: 10
0 1 1 2 3 5 8 13 21 34
"""
