from Exercise.Wild_Farm.project.animals.animal import Mammal


class Mouse(Mammal):
    allowed_foods = ['Vegetable', 'Fruit']
    weight_increase = 0.10

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    allowed_foods = ['Meat']
    weight_increase = 0.40

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    allowed_foods = ['Vegetable', 'Meat']
    weight_increase = 0.30

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    allowed_foods = ['Meat']
    weight_increase = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"
