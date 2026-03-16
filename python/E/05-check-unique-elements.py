numbers = [1, 2, 3, 4, 5, 1]
is_unique = True

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            is_unique = False
            break
    if not is_unique:
        break

print("List:", numbers)
if is_unique:
    print("All elements are unique")
else:
    print("Elements are not unique")

"""
List: [1, 2, 3, 4, 5, 1]
Elements are not unique
"""
