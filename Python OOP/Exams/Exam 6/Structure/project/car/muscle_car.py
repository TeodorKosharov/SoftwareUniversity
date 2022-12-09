from project.car.car import Car


class MuscleCar(Car):
    max_speed_limit = 450
    min_speed_limit = 250

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False
