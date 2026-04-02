def circle_values(radius):
    pi = 3.14
    diameter = 2 * radius
    area = pi * radius * radius
    return diameter, area


r = float(input("Enter radius: "))
diameter, area = circle_values(r)
print(f"Diameter of circle: {diameter}")
print(f"Area of circle: {area}")

"""
Enter radius: 5
Diameter of circle: 10.0
Area of circle: 78.5
"""
