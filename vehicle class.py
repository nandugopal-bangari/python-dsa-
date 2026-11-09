class Vehicle:
    brand="BMW"
    Model="M4"
    def display_details(self):
        print("Best Luxury car")
class Car(Vehicle):
    speed=400
    mileage=10
class Bike(Vehicle):
    name = "Kawasaki"
    variant = "Z900"
 
b=Bike()
C=Car()
b.display_details()
C.display_details()
print(b.name)
print(C.speed)
    
    