student_marks = {"Aman": 85, "Riya": 90, "Karan": 78}
inverted_dict = {}

for key, value in student_marks.items():
    inverted_dict[value] = key

print("Original dictionary:", student_marks)
print("Inverted dictionary:", inverted_dict)

"""
Original dictionary: {'Aman': 85, 'Riya': 90, 'Karan': 78}
Inverted dictionary: {85: 'Aman', 90: 'Riya', 78: 'Karan'}
"""
