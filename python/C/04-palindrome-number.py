num = int(input("Enter a number: "))

temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num == reverse:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")

"""
Enter a number: 121
121 is a palindrome number
"""

"""
# another way using string reverse using [-1]

num = int(input("Enter a number: "))
reverse = str(num)[::-1]

if num == int(reverse):
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")

"""
