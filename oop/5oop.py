# OOP Exercise 5: Define a property that must have the same value for every class instance (object)

# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
# class Bus(Vehicle):
#     pass
# class Car(Vehicle):
#     pass

# Expected Output:

# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

class Vehicle:
    vehicle_color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def __str__(self):
        return (f"Color: {Vehicle.vehicle_color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")
class Bus(Vehicle):
    pass
class Car(Vehicle):
    pass

school_bus = Bus("School Volvo", 180, 12)
print(school_bus)
audi = Car("Audi Q5", 240, 18)
print(audi)
