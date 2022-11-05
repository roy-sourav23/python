# OOP Exercise 1: Create a Class with instance attributes

# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage) -> None:
        self.max_speed = max_speed
        self.mileage = mileage
    
f77 = Vehicle(147, 150)
print(f77.max_speed, f77.mileage)