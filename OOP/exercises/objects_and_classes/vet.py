class Vet:
    animals = []
    space = 5

    def __init__(self, name: str) -> None:
        self.name = name
        self.animals = []

    def register_animal(self, animal_name: str) -> str:
        if self.__class__.space > len(self.__class__.animals):
            self.__class__.animals.append(animal_name)
            self.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name in self.__class__.animals:
            self.__class__.animals.remove(animal_name)
            self.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"

        return f"{animal_name} not in the clinic"

    def info(self):
        space_left = self.__class__.space - len(self.__class__.animals )
        return f"{self.name} has {len(self.animals)} animals. {space_left} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())