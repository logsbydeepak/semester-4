print("Prime numbers less than 20:")

for num in range(2, 20):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)


"""
Prime numbers less than 20:
2
3
5
7
11
13
17
19
"""
