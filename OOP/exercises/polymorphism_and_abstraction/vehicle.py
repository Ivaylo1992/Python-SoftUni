from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int) -> None:
        needed_fuel = distance * (self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION)
        if needed_fuel < self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int) -> None:
        needed_fuel = distance * (self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION)
        if needed_fuel < self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel * 0.95

car = Car(20, 5)

car.drive(3)

print(car.fuel_quantity)

car.refuel(10)

print(car.fuel_quantity)

truck = Truck(100, 15)

truck.drive(5)

print(truck.fuel_quantity)

truck.refuel(50)

print(truck.fuel_quantity)

