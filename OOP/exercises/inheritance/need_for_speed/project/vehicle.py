class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25
    def __init__(self, fuel: float, horse_power: int) -> None:
        self.fuel_consumption: float = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers: float) -> None:
        needed_fuel = kilometers * self.fuel_consumption
        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel