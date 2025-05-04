from OOP.lab.inheritance.multiple_inheritance.project.employee import Employee
from OOP.lab.inheritance.multiple_inheritance.project.person import Person


class Teacher(Employee, Person):
    def __init__(self):
        super().__init__()

    def teach(self):
        return 'teaching...'