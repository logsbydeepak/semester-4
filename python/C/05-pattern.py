rows = 5

for i in range(1, rows + 1):
    for _ in range(i):
        print("*", end="")
    print()

for i in range(rows, 0, -1):
    for _ in range(i):
        print("*", end="")
    print()


"""
*
**
***
****
*****
*****
****
***
**
*
"""

"""
# another way

n = 5
for i in range(1, n + 1):
    print("*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i)

"""
