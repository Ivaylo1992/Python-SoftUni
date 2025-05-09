from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(
            self, name: str, budget: int,
            animal_capacity: int, workers_capacity: int
    ) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget < price:
            return "Not enough budget"

        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        needed_money = sum([worker.salary for worker in self.workers])

        if needed_money > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed_money
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        needed_money = sum([a.money_for_care for a in self.animals])

        if needed_money <= self.__budget:
            self.__budget -= needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        _animal_types = ['Lion', 'Tiger', 'Cheetah']

        total_animals_count = len(self.animals)
        result = [f'You have {total_animals_count} animals']

        for animal in _animal_types:
            result.extend(self.get_info(animal, self.animals))

        return "\n".join(result)

    def workers_status(self) -> str:
        _workers_types = ['Keeper', 'Caretaker', 'Vet']

        total_workers_count = len(self.workers)
        result = [f'You have {total_workers_count} workers']

        for w in _workers_types:
            result.extend(self.get_info(w, self.workers))

        return "\n".join(result)

    @staticmethod
    def get_info(type_name: str, types_list: list):
        """
            Returns information about a particular type (animal or worker)
            depending on the method it is called from.
        """
        info = []
        type_list = [t for t in types_list if t.__class__.__name__ == type_name]

        count = len(type_list)
        info.append(f"----- {count} {type_name}s:")

        for t in type_list:
            info.append(t.__repr__())

        return info


