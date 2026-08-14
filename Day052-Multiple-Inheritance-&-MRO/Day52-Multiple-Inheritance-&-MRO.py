# Day 52: Multiple Inheritance & MRO 
class Vehicle:
    def start(self):
        print("Vehicle is starting")

    def info(self):
        print("This is a vehicle")


class Flyable:
    def fly(self):
        print("This object can fly")

    def info(self):
        print("This is a flyable object")


class FlyingCar(Vehicle, Flyable):
    pass

car = FlyingCar()

car.start()
car.fly()
car.info()   # Python will call the method based on MRO

print(FlyingCar.mro())