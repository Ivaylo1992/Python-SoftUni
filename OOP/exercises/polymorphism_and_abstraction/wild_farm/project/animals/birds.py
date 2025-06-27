from project.animals.animal import Bird
from project.food import Food, Meat, Fruit, Seed, Vegetable


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    @property
    def gained_weight(self):
        return 0.25

    @property
    def what_eats(self):
        return [Meat]

class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    @property
    def gained_weight(self):
        return 0.35

    @property
    def what_eats(self):
        return [Vegetable, Fruit, Meat, Seed]