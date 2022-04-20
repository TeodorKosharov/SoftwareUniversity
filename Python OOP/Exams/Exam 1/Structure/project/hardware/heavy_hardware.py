from project.hardware.hardware import Hardware
import math


class HeavyHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, 'Heavy', capacity * 2, math.floor(memory * 0.75))
