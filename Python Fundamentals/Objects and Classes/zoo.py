class Zoo:
    __animals = 0   # class attribute

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.birds = []
        self.fishes = []

    def add_animal(self, species, name):
        self.__animals += 1
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

    def get_info(self, species):
        animals_name = None
        ress = ''

        if species == 'mammal':
            animals_name = self.mammals
            ress = 'Mammals'
        elif species == 'fish':
            animals_name = self.fishes
            ress = 'Fishes'
        elif species == 'bird':
            animals_name = self.birds
            ress = 'Birds'

        animals_data = ', '.join(animals_name)
        return f"""{ress} in {self.name}: {animals_data}
Total animals: {self.__animals}"""


zoo_name = input()
n = int(input())
zoo = Zoo(zoo_name)

for line in range(n):
    info = input().split()
    zoo.add_animal(info[0], info[1])

spesies_type = input()
res = zoo.get_info(spesies_type)
print(res)


