class A:
    def rk(self):
        print("In class A")

class B(A):
    def rk(self):
        print("In class B")

r = B()
r.rk()
