text = input("Enter a string: ")
text = text.lower()
reverse = text[::-1]

if text == reverse:
    print(f'"{text}" is a palindrome string')
else:
    print(f'"{text}" is not a palindrome string')

"""
Enter a string: madam
"madam" is a palindrome string
"""

"""
# another way

text = input("Enter a string: ").lower()
is_palindrome = True

for i in range(len(text)):
    if text[i] != text[len(text) - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print(f'"{text}" is a palindrome string')
else:
    print(f'"{text}" is not a palindrome string')

"""
