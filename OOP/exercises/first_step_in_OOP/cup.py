class Cup:
    def __init__(self, size, quantity):
        self.size: int = size
        self.quantity: int = quantity

    def fill(self, quantity):
        if  not (self.status() < quantity):
            self.quantity += quantity

    def status(self):
        return self.size - self.quantity

cup = Cup(100, 50)

print(cup.status())
cup.fill(40)

cup.fill(20)

print(cup.status())