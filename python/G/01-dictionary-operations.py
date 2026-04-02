student = {"name": "Aman", "age": 20, "course": "BCA"}
print("Original dictionary:", student)

student["age"] = 21
student["city"] = "Delhi"
print("After update and add:", student)

removed_value = student.pop("course")
print("Removed value of 'course':", removed_value)
print("Dictionary after removal:", student)

print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

"""
Original dictionary: {'name': 'Aman', 'age': 20, 'course': 'BCA'}
After update and add: {'name': 'Aman', 'age': 21, 'course': 'BCA', 'city': 'Delhi'}
Removed value of 'course': BCA
Dictionary after removal: {'name': 'Aman', 'age': 21, 'city': 'Delhi'}
Keys: ['name', 'age', 'city']
Values: ['Aman', 21, 'Delhi']
"""
