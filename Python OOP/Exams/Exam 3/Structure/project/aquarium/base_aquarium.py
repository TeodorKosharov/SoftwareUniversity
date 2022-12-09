from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Aquarium name cannot be an empty string.')
        self.__name = value

    def calculate_comfort(self):
        return sum([x.comfort for x in self.decorations])

    def add_fish(self, fish):
        if len(self.fish) <= self.capacity:
            self.fish.append(fish)
            self.capacity -= 1
            return f'Successfully added {type(fish).__name__} to {self.name}.'
        return 'Not enough capacity.'

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fishs in self.fish:
            fishs.eat()

    def __str__(self):
        result = f'{self.name}:\n'
        if self.fish:
            result += f'Fish: {" ".join([fishs.name for fishs in self.fish])}\n'
        elif not self.fish:
            result += 'Fish: none\n'
        result += f'Decorations: {len(self.decorations)}\n'
        result += f'Comfort: {sum([decoration.comfort for decoration in self.decorations])}'

        return result
