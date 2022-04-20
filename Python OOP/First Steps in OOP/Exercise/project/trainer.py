from Exercise.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name):
        for current_pokemon in self.pokemons:
            if pokemon_name == current_pokemon.name:
                self.pokemons.remove(current_pokemon)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}" + "\n" + f"Pokemon count {len(self.pokemons)}" + "\n"

        for pokemon_data in self.pokemons:
            result += f'- {pokemon_data.pokemon_details()}' + '\n'

        return result
