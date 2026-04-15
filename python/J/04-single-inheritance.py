class A:
    def show_a(self):
        print("This is parent class")


class B(A):
    def show_b(self):
        print("This is child class")


b = B()
b.show_a()
b.show_b()

"""
This is parent class
This is child class
"""
