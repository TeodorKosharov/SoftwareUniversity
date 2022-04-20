from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if model in [x.model for x in self.cars]:
            raise Exception(f"Car {model} is already created!")
        if car_type == 'MuscleCar':
            car = MuscleCar(model, speed_limit)
        elif car_type == 'SportsCar':
            car = SportsCar(model, speed_limit)
        else:
            return None
        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [x.name for x in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")
        created_driver = Driver(driver_name)
        self.drivers.append(created_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [x.name for x in self.races]:
            raise Exception(f"Race {race_name} is already created!")
        created_race = Race(race_name)
        self.races.append(created_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if driver_name not in [x.name for x in self.drivers]:
            raise Exception(f"Driver {driver_name} could not be found!")
        driver = [x for x in self.drivers if x.name == driver_name][0]
        for index in range(len(self.cars) - 1, -1, -1):
            current_car = self.cars[index]
            if type(current_car).__name__ == car_type and not current_car.is_taken:
                chosen_car = current_car
                break
        else:
            raise Exception(f"Car {car_type} could not be found!")

        chosen_car.is_taken = True
        if driver.car is not None:
            old_car = type(driver.car).__name__
            driver.car = chosen_car
            return f"Driver {driver.name} changed his car from {old_car} to {type(chosen_car).__name__}."
        driver.car = chosen_car
        return f"Driver {driver_name} chose the car {type(chosen_car).__name__}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if race_name not in [x.name for x in self.races]:
            raise Exception(f"Race {race_name} could not be found!")
        if driver_name not in [x.name for x in self.drivers]:
            raise Exception(f"Driver {race_name} could not be found!")
        driver = [x for x in self.drivers if x.name == driver_name][0]
        race = [x for x in self.races if x.name == race_name][0]

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if race_name not in [x.name for x in self.races]:
            raise Exception(f"Race {race_name} could not be found!")
        race = [x for x in self.races if x.name == race_name][0]
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        self.drivers = sorted(self.drivers, key=lambda x: x.car.speed_limit, reverse=True)
        counter = 0
        result = ''
        for driver in self.drivers:
            result += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"
            driver.number_of_wins += 1
            if counter == 2:
                break
            counter += 1
        return result
