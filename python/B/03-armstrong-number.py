num = int(input("Enter a number: "))
temp = num
count = 0

while temp:
    count += 1
    temp //= 10

temp = num
total = 0

while temp:
    digit = temp % 10
    total += digit**count
    temp //= 10

if total == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

"""
Enter a number: 153
153 is an Armstrong number
"""
