from OOP.exercises.first_step_in_OOP.pokemon_battle.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: list[Pokemon] = []

    def add_pokemon(self, pokemon_to_catch: Pokemon) -> str:
        for pok in self.pokemons:
            if pok.name == pokemon_to_catch.name:
                return "This pokemon is already caught"

        self.pokemons.append(pokemon_to_catch)
        return 'Caught ' + pokemon_to_catch.pokemon_details()

    def release_pokemon(self, pokemon_name: str) -> str:
        for pok in self.pokemons:
            if pok.name == pokemon_name:
                self.pokemons.remove(pok)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        result = [
            f'Pokemon Trainer {self.name}',
            f'Pokemon count {len(self.pokemons)}'
        ]

        for pok in self.pokemons:
            result.append('- ' + pok.pokemon_details())

        return "\n".join(result)
