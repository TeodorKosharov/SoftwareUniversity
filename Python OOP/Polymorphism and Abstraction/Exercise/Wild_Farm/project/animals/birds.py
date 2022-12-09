from Exercise.Wild_Farm.project.animals.animal import Bird


class Owl(Bird):
    allowed_foods = ['Meat']
    weight_increase = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    allowed_foods = ['Vegetable', 'Fruit', 'Meat', 'Seed']
    weight_increase = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"
