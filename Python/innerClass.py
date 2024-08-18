class Student():
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno    
        self.lapt = self.Laptop()
    def show1(roll):
        rollno = roll
        return rollno

    def show(self):
        print(self.name, self.rollno)
        self.lapt.show()

    class Laptop():
        def __init__(self):
            self.brand = "lenovo"
            self.ram = 8
            self.cpu = "i7"

        def show(self):
            print(self.brand,self.ram,self.cpu)

s1 = Student("Sera",68)
s1.show()
print(s1.show1(23))
# This shows that python methods can't work without self