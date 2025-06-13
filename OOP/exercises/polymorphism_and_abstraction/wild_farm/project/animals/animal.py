from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.food_eaten = 0


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: int, wing_size: float) -> None:
        super().__init__(name, weight)
        self.wing_size = wing_size

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: int, living_region: str) -> None:
        super().__init__(name, weight)
        self.living_region = living_region

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"




