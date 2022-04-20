from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    completed_missions = 0
    failed_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type == 'Biologist':
            created_astronaut = Biologist(name)
        elif astronaut_type == 'Geodesist':
            created_astronaut = Geodesist(name)
        elif astronaut_type == 'Meteorologist':
            created_astronaut = Meteorologist(name)
        else:
            raise Exception("Astronaut type is not valid!")

        if created_astronaut.name not in [x.name for x in self.astronaut_repository.astronauts]:
            self.astronaut_repository.astronauts.append(created_astronaut)
            return f"Successfully added {astronaut_type}: {created_astronaut.name}."
        return f"{created_astronaut.name} is already added."

    def add_planet(self, name: str, items: str):
        created_planet = Planet(name)
        created_planet.items = items.split(', ')
        if name not in [x.name for x in self.planet_repository.planets]:
            self.planet_repository.planets.append(created_planet)
            return f"Successfully added Planet: {name}."
        return f"{name} is already added."

    def retire_astronaut(self, name: str):
        if name not in [x.name for x in self.astronaut_repository.astronauts]:
            raise Exception(f"Astronaut {name} doesn't exist!")
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                self.astronaut_repository.astronauts.remove(astronaut)
                return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        if planet_name not in [x.name for x in self.planet_repository.planets]:
            raise Exception("Invalid planet name!")
        chosen_planet = [x for x in self.planet_repository.planets if x.name == planet_name][0]
        available_astronauts_above_30_oxygen = []

        for astronaut in sorted(self.astronaut_repository.astronauts, key=lambda x: x.oxygen, reverse=True):
            if len(available_astronauts_above_30_oxygen) == 5:
                break
            if astronaut.oxygen > 30:
                self.astronaut_repository.astronauts.remove(astronaut)
                available_astronauts_above_30_oxygen.append(astronaut)

        if not available_astronauts_above_30_oxygen:
            raise Exception("You need at least one astronaut to explore the planet!")

        planet_items_available = True if chosen_planet.items else False
        astronauts_in_space = 0
        for astronaut in available_astronauts_above_30_oxygen:
            astronauts_in_space += 1

            while astronaut.oxygen > 0:
                if chosen_planet.items:
                    astronaut.breathe()
                    picked_item = chosen_planet.items.pop()
                    astronaut.backpack.append(picked_item)
                else:
                    planet_items_available = False
                    break
            if not planet_items_available:
                break

        if planet_items_available:
            SpaceStation.failed_missions += 1
            return "Mission is not completed."
        SpaceStation.completed_missions += 1
        return f"Planet: {planet_name} was explored. {astronauts_in_space} astronauts participated in collecting items."

    def report(self):
        result = f"{SpaceStation.completed_missions} successful missions!\n"
        result += f"{SpaceStation.failed_missions} missions were not completed!\n"
        result += "Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += f"Name: {astronaut.name}\n"
            result += f"Oxygen: {astronaut.oxygen}\n"
            if astronaut.backpack:
                result += f"Backpack items: {', '.join(astronaut.backpack)}\n"
            else:
                result += 'Backpack items: none\n'
        return result
