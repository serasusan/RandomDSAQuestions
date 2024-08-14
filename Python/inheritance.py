class C:
    def __init__(self):
        print("In class C")

class A():
    def __init__(self):
        print("in class A")


class B(C,A):
    def __init__(self):
        super().__init__()
        
        print("in Class B")
        

b = B()