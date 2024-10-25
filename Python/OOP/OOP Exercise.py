class Vehicle:
    def __init__(self, name, maxspeed, mileage, capacity):
        self.name = name
        self.max_speed = maxspeed
        self.mileage = mileage
        self.colour = 'White'
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def fare(self):
        return self.capacity* 100

class Bus(Vehicle):
    def fare(self):
        base = self.capacity *100
        total = base + base/10
        return total

class Car(Vehicle):
    pass

schoolbus = Bus("Volvo Civic", 120, 12, 50)
car = Car("RB20", 340, 18, 4)
print(f'Colour:{schoolbus.colour} Name:{schoolbus.name} Speed:{schoolbus.max_speed} Mileage:{schoolbus.mileage}')
print(f'Colour:{car.colour} Name:{car.name} Speed:{car.max_speed} Mileage:{car.mileage}')
print(car.fare())
print(schoolbus.fare())
print(type(schoolbus))
print(isinstance(schoolbus, Vehicle))