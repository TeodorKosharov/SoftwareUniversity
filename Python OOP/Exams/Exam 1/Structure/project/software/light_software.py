from project.software.software import Software
import math


class LightSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, 'Light', math.floor(capacity_consumption + 0.50 * capacity_consumption),
                         math.floor(memory_consumption - memory_consumption * 0.50))
