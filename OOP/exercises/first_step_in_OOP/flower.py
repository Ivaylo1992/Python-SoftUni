class Flower:
    def __init__(self, name, water_requirements) -> None:
        self.name: str = name
        self.water_requirements: int = water_requirements
        self.is_happy = False

    def water(self, quantity: int) -> None:
        self.is_happy = quantity >= self.water_requirements

    def status(self) -> str:
        happiness_status = 'is happy' if self.is_happy else 'is not happy'
        return f'{self.name} {happiness_status}'


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())



