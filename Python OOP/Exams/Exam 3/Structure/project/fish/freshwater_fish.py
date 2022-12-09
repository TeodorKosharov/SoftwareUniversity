from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    valid_aquarium = 'FreshwaterAquarium'

    def __init__(self, name, species, price):
        super().__init__(name, species, 3, price)

    def eat(self):
        self.size += 3
