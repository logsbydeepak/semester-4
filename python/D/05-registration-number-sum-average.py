registration_number = input("Enter your registration number: ")
digit_sum = 0
digit_count = 0

for char in registration_number:
    if char.isdigit():
        digit_sum += int(char)
        digit_count += 1

if digit_count == 0:
    print("No digits found in registration number")
else:
    average = digit_sum / digit_count
    print(f"Sum of digits: {digit_sum}")
    print(f"Average of digits: {average:.2f}")

"""
Enter your registration number: 22BCS10452
Sum of digits: 16
Average of digits: 2.29
"""
