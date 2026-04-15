class Stu:
    def __init__(self, n, m):
        self.name = n
        self.mark = m

    def grade(self):
        if self.mark >= 80:
            return "Excellent"
        if self.mark >= 65:
            return "Good"
        if self.mark >= 50:
            return "Pass"
        return "Fail"


n = input("Enter name: ")
m = int(input("Enter marks: "))
s = Stu(n, m)

print("Grade:", s.grade())

"""
Enter name: Amit
Enter marks: 85
Grade: Excellent
"""
