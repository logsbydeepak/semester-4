class A:
    def show_a(self):
        print("This is first parent")


class B:
    def show_b(self):
        print("This is second parent")


class C(A, B):
    def show_c(self):
        print("This is child")


c = C()
c.show_a()
c.show_b()
c.show_c()

"""
This is first parent
This is second parent
This is child
"""
