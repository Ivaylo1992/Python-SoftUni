from project.elf import Elf


class MuseElf(Elf):
    def __init__(self, username: str, level: int) -> None:
        super().__init__(username, level)