from OOP.exercises.polymorphism_and_abstraction.wild_farm.project.animals.animal import Bird
from OOP.exercises.polymorphism_and_abstraction.wild_farm.project.food import Food, Meat


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.25 * food.quantity


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.food_eaten += food.quantity
        self.weight += 0.35 * food.quantity