# Inheritance - Advanced (Single Inheritance) :
#Over-Riding init Method:
# Create a Class and define its fuctions :
class Vehicle:
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def show_vehicle_details(self):
        print("I am a Vehicle")
        print("Mileage of Vehice is ", self.mileage)
        print("Cost of Vehicle is ", self.cost)

class Car(Vehicle):
    def __init__(self, mileage, cost, tyres, hp):
        super().__init__(mileage,
                       cost)
        # With this, we are telling the program that use data for mileage and cost from vehicle class as they are already defined before. i.e., Over-Riding 
        self.tyres = tyres
        self.hp = hp

    def show_car_details(self):
        print("I am a Car")
        print("Number of Tyres in Car:", self.tyres)
        print("Horse Power of Car : ", self.hp)


c1 = Car(600, 450000, 4, 9900)
c1.show_vehicle_details()
c1.show_car_details()


