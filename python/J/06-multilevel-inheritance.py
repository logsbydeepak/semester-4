class A:
    def show_a(self):
        print("This is grandparent")


class B(A):
    def show_b(self):
        print("This is parent")


class C(B):
    def show_c(self):
        print("This is child")


c = C()
c.show_a()
c.show_b()
c.show_c()

"""
This is grandparent
This is parent
This is child
"""
