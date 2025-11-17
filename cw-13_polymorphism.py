class Vehicle:
    def __init__(self, ma, mod, col):
        self._make = ma
        self._model = mod
        self._color = col

    def display(self):
        print("Car Make: ", self._make)
        print("Car Model: ", self._model)
        print("Car Color: ", self._color)

class Car(Vehicle):
    def __init__(self, x, y, z):
        Vehicle.__init__(self, x, y, z)

    def display(self):
        print(Vehicle.display(self))


class Truck(Vehicle):
    def __init__(self, x, y, z):
        Vehicle.__init__(self, x, y, z)

    def display(self):
        print(Vehicle.display(self))


c1 =Car("Volkswagon", "Beetle", "Blue")
c1.display()

t1 =Truck("Ford", "F150", "Pink")
t1.display()