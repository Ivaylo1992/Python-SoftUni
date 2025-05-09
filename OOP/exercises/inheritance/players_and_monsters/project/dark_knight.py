from project.knight import Knight


class DarkKnight(Knight):
    def __init__(self, username: str, level: int) -> None:
        super().__init__(username, level)