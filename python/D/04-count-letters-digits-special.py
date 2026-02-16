text = input("Enter a string: ")
letters = 0
digits = 0
special_symbols = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        special_symbols += 1

print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Special symbols: {special_symbols}")

"""
Enter a string: Abc@123!
Letters: 3
Digits: 3
Special symbols: 2
"""
