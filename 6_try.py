class Car:
    def infor(self):
        print("This is a car")

car = Car()
car.infor()

isinstance(car, Car)
isinstance(car, str)

if 5 > 3:
    pass

class A:
    def __init__(self, value1=0, value2=0):
        self._value1 = value1
        self.__value2 = value2

    def setValue(self, value1, value2):
        self._value1 = value1
        self.__value2 = value2

    def show(self):
        print(self._value1)
        print(self.__value2)

a = A()
print(a._value1)
print(a._A__value2)
