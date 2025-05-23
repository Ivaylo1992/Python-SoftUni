class Room:
    def __init__(self, number: int, capacity: int) -> None:
        self.number = number
        self.capacity = capacity
        self.is_taken = False
        self.guests = 0

    def take_room(self, people: int) -> str | None:
        if not self.is_taken and people <= self.capacity:
            self.is_taken = True
            self.guests += people

        return f"Room number {self.number} cannot be taken"

    def free_room(self) -> str | None:
        if not self.is_taken:
            return f"Room number {self.number} is not taken"

        self.guests = 0
        self.is_taken = False
        return None
