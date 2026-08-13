# 3. Vehicle System — Inheritance Concept: Inheritance Create a parent class Vehicle and child classes Car, Bike and Truck.
# Vehicle should contain common properties such as brand, speed and fuel. Each child class must have at least one unique property:
# • Car — numberOfDoors • Bike — hasGear • Truck — loadCapacity Create objects of all three classes and display their information.

class Vehicle:

    def __init__(self, brand, speed, fuel):
        self.brand = brand
        self.speed = speed
        self.fuel = fuel

    def display(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed, "km/h")
        print("Fuel:", self.fuel)


class Car(Vehicle):

    def __init__(self, brand, speed, fuel, numberOfDoors):
        super().__init__(brand, speed, fuel)
        self.numberOfDoors = numberOfDoors

    def display(self):
        super().display()
        print("Number of Doors:", self.numberOfDoors)


class Bike(Vehicle):

    def __init__(self, brand, speed, fuel, hasGear):
        super().__init__(brand, speed, fuel)
        self.hasGear = hasGear

    def display(self):
        super().display()
        print("Has Gear:", self.hasGear)
class Truck(Vehicle):

    def __init__(self, brand, speed, fuel, loadCapacity):
        super().__init__(brand, speed, fuel)
        self.loadCapacity = loadCapacity

    def display(self):
        super().display()
        print("Load Capacity:", self.loadCapacity, "tons")
car = Car("Toyota", 180, "Petrol", 4)
bike = Bike("Yamaha", 120, "Petrol", True)
truck = Truck("Volvo", 100, "Diesel", 20)
print("CAR")
car.display()

print("\nBIKE")
bike.display()

print("\nTRUCK")
truck.display()
