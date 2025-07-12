from abc import abstractmethod, ABC

class Animal(ABC):
    ...

class SilentAnimal(Animal):
    @abstractmethod
    def be_scary(self):
        pass


class SoundAnimal(Animal):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(SoundAnimal):
    def make_sound(self):
        return 'woof-woof'

    def sniffing_for_people(self):
        return "sniffing for missing persons"


class Cat(SoundAnimal):
    def make_sound(self):
        return 'meow'


class Pig(SoundAnimal):
    def make_sound(self):
        return 'oink'


class Snake(SilentAnimal):
    def be_scary(self):
        return 'looks green'


def animal_sound(animals: list[Animal]):
    for animal in animals:
        print(animal.make_sound())


print(SoundAnimal.__mro__)




## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
