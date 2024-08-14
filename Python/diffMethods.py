class Car:
    wheel = 4

    def __init__(self,mileage, company = "Honda"): #instance method
        self.mileage = mileage
        self.company = company

    def brandDetails(self): #instance method
        return str(self.mileage)+ " " + self.company
    
    @classmethod
    def getWheel(cls): #class nethod
        return cls.wheel
    
    # @staticmethod
    def info():
        print("hii")


c1 = Car(10)
print(c1.brandDetails())
print(Car.brandDetails(c1))
print(c1.getWheel())
print(Car.getWheel())
# print(Car.getWheel())
# c1.info()
Car.info()