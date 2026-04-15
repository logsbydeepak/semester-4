class Stu:
    def set_name(self, n):
        self.name = n

    def get_name(self):
        return self.name


s = Stu()
s.set_name("Amit")
print("Name:", s.get_name())

"""
Name: Amit
"""
