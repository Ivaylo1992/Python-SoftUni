from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int) -> "Hotel":
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)
                self.guests += people

    def free_room(self, room_number: int) -> None:
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()


    def status(self):
        result = []
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]

        result.append(f'Hotel {self.name} has {self.guests} total guests')
        result.append(f'Free rooms: {", ".join(free_rooms)}')
        result.append(f'Taken rooms: {", ".join(taken_rooms)}')

        return '\n'.join(result)




