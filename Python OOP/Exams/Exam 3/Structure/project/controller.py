from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type != 'FreshwaterAquarium' or aquarium_type != 'SaltwaterAquarium':
            return 'Invalid aquarium type.'
        new_aquarium = FreshwaterAquarium(
            aquarium_name) if aquarium_type == 'FreshwaterAquarium' else SaltwaterAquarium(aquarium_name)
        self.aquariums.append(new_aquarium)
        return f'Successfully added {aquarium_type}.'

    def add_decoration(self, decoration_type: str):
        if decoration_type != 'Ornament' or decoration_type != 'Plant':
            return 'Invalid decoration type.'
        new_decor = Ornament() if decoration_type == 'Ornament' else Plant()
        self.decorations_repository.decorations.append(new_decor)
        return f'Successfully added {decoration_type}.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        is_aquarium_there = False
        is_decor_there = False
        chosen_aquarium = ''
        chosen_decor = ''

        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                is_aquarium_there = True
                chosen_aquarium = aquarium
                break

        for decoration in self.decorations_repository.decorations:
            if type(decoration).__name__ == decoration_type:
                is_decor_there = True
                chosen_decor = decoration
                break

        if is_aquarium_there and is_decor_there:
            chosen_aquarium.decorations.append(chosen_decor)
            self.decorations_repository.decorations.remove(chosen_decor)
            return f'Successfully added {decoration_type} to {aquarium_name}.'
        return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type != 'FreshwaterFish' or fish_type != 'SaltwaterFish':
            return f"There isn't a fish of type {fish_type}."

        chosen_fish = FreshwaterFish(fish_name, fish_species,
                                     price) if fish_type == 'FreshwaterFish' else SaltwaterFish(fish_name, fish_species,
                                                                                                price)
        chosen_aquarium = [x.name for x in self.aquariums if x.name == aquarium_name][0]
        if chosen_aquarium.capacity == 0:
            return f'Not enough capacity.'
        elif chosen_fish.valid_aquarium != type(chosen_aquarium).__name__:
            return 'Water not suitable.'

        chosen_aquarium.fish.append(chosen_fish)
        return f'Successfully added {fish_type} to {aquarium_name}.'

    def feed_fish(self, aquarium_name: str):
        chosen_aquarium = [x.name for x in self.aquariums if x.name == aquarium_name][0]
        fed_fish = 0
        for fish in chosen_aquarium.fish:
            fish.eat()
            fed_fish += 1
        return f'Fish fed: {fed_fish}'

    def calculate_value(self, aquarium_name: str):
        chosen_aquarium = [x.name for x in self.aquariums if x.name == aquarium_name][0]
        total_value = 0
        for decor in chosen_aquarium.decorations:
            total_value += decor.price
        for fish in chosen_aquarium.fish:
            total_value += fish.price
        return f'The value of Aquarium {aquarium_name} is {total_value:.2f}.'

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += f'{aquarium.name}:\n'
            result += str(aquarium) + '\n'
        return result
