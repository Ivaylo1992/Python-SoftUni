class Equipment:
    id = 1
    def __init__(self, name: str) -> None:
        self.name = name
        self.id = self.__class__.id
        self.__class__.id += 1

    @staticmethod
    def get_next_id():
        return Equipment.id

    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"
