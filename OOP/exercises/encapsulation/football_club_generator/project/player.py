
class Player:
    def __init__(
            self, name: str, sprint: int, dribble: int,
            passing: int, shooting: int
    ) -> None:
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self) -> str:
        return (
            f"Player: {self.__name}\n"
            f"Sprint: {self.__sprint}\n"
            f"Dribble: {self.__dribble}\n"
            f"Passing: {self.__passing}\n"
            f"Shooting: {self.__shooting}"
        )

    @property
    def name(self) -> str:
        return self.__name

