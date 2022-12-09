from Exercise.Wild_Cat_Zoo.project.animal import Animal
from Exercise.Wild_Cat_Zoo.project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif self.__animal_capacity > 0:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for current_worker in self.workers:
            if current_worker.name == worker_name:
                self.workers.remove(current_worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        if self.__budget >= sum([x.salary for x in self.workers]):
            self.__budget -= sum([x.salary for x in self.workers])
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        if self.__budget >= sum([x.money_for_care for x in self.animals]):
            self.__budget -= sum([x.money_for_care for x in self.animals])
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [x for x in self.animals if type(x).__name__ == 'Lion']
        tigers = [x for x in self.animals if type(x).__name__ == 'Tiger']
        cheetahs = [x for x in self.animals if type(x).__name__ == 'Cheetah']

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += lion.__repr__() + "\n"
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += tiger.__repr__() + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += cheetah.__repr__() + "\n"

        return result.strip()

    def workers_status(self):
        keepers = [x for x in self.workers if type(x).__name__ == 'Keeper']
        caretakers = [x for x in self.workers if type(x).__name__ == 'Caretaker']
        vets = [x for x in self.workers if type(x).__name__ == 'Vet']

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += keeper.__repr__() + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += caretaker.__repr__() + "\n"
        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += vet.__repr__() + "\n"

        return result.strip()
