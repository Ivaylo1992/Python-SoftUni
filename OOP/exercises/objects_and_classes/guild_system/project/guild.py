from OOP.exercises.objects_and_classes.guild_system.project.player import Player


class Guild:
    def __init__(self, name: str) -> None:
        self.name = name
        self.players: list[Player] = []

    def assign_player(self, p: Player) -> str:
        if p.guild == self.name:
            return f"Player {p.name} is already in the guild."

        if player.guild != 'Unaffiliated':
            return f"Player {p.name} is in another guild."

        self.players.append(p)
        p.guild = self.name
        return f"Welcome player {p.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for p in self.players:
            if p.name == player_name:
                self.players.remove(p)
                p.guild = 'Unaffiliated'
                return f"Player {player_name} has been kicked from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        result = f'Guild: {self.name}\n'

        for p in self.players:
            result += f'{p.player_info()}\n'

        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
print(guild.kick_player("George"))
print(player.player_info())