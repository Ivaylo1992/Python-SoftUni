class SteamUser:
    def __init__(self, username: str, games: list) -> None:
        self.username = username
        self.games = games
        self.played_hours: int = 0

    def play(self, game: str, hours: int) -> str:
        if game not in self.games:
            return f"{game} is not in library"
        else:
            self.played_hours += hours
            return f"{self.username} is playing {game}"

    def buy_game(self, game: str) -> str:
        if game in self.games:
            return f"{game} is already in your library"
        else:
            self.games.append(game)
            return f"{self.username} bought {game}"

    def status(self) -> str:
        games_count = len(self.games)
        return f"{self.username} has {games_count} games. Total play time: {self.played_hours}"