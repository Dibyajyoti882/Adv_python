# Vehicle Rental System Problem: Create a rental system with a base class Vehicle and subclasses Car, Bike, and Truck. Include a rental rate for each and calculate the rental fee using overridden methods. Use class variables to track total vehicles rented.
class Vehicle:
    total_rented = 0

    def rent(self, days):
        pass


class Car(Vehicle):
    def rent(self, days):
        Vehicle.total_rented += 1
        return 100 * days


class Bike(Vehicle):
    def rent(self, days):
        Vehicle.total_rented += 1
        return 50 * days


while True:
    print("\n1. Rent Car")
    print("2. Rent Bike")
    print("3. Show Total Rented")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        days = int(input("Enter days: "))
        c = Car()
        print("Total Rent:", c.rent(days))

    elif ch == 2:
        days = int(input("Enter days: "))
        b = Bike()
        print("Total Rent:", b.rent(days))

    elif ch == 3:
        print("Total Vehicles Rented:", Vehicle.total_rented)

    elif ch == 4:
        break

    else:
        print("Invalid choice")