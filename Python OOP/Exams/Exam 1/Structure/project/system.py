from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def get_hardware():
        return System._hardware

    @staticmethod
    def get_software():
        return System._software

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        res = System.get_hardware()
        res.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        res = System.get_hardware()
        res.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardwares = System.get_hardware()
        if hardware_name not in [x.name for x in hardwares]:
            return 'Hardware does not exist'
        else:
            current_hardware = [x for x in hardwares if x.name == hardware_name][0]
            express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            current_hardware.install(express_software)
            softwares = System._software
            softwares.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardwares = System.get_hardware()
        if hardware_name not in [x.name for x in hardwares]:
            return 'Hardware does not exist'
        else:
            current_hardware = [x for x in hardwares if x.name == hardware_name][0]
            light_software = LightSoftware(name, capacity_consumption, memory_consumption)
            current_hardware.install(light_software)
            softwares = System._software
            softwares.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardwares = System.get_hardware()
        softwares = System.get_software()

        if hardware_name not in [x.name for x in hardwares] or software_name not in [x.name for x in softwares]:
            return 'Some of the components do not exist'
        else:
            hardware = [x for x in hardwares if x.name == hardware_name][0]
            software = [x for x in softwares if x.name == software_name][0]
            hardware.uninstall(software)
            softwares.remove(software)

    @staticmethod
    def analyze():
        hardwares = System.get_hardware()
        hardwares_total_components = len(hardwares)
        total_memory_all_hardware_components = sum([x.memory for x in hardwares])
        total_capacity_all_hardware_components = sum([x.capacity for x in hardwares])

        softwares = System.get_software()
        softwares_total_components = len(softwares)
        total_memory_all_software_components = sum([x.memory for x in softwares])
        total_capacity_all_software_components = sum([x.capacity for x in softwares])

        result = 'System Analysis\n'
        result += f'Hardware Components: {hardwares_total_components}\n'
        result += f'Software Components: {softwares_total_components}\n'
        result += f'Total Operational Memory: {total_memory_all_software_components} / {total_memory_all_hardware_components}\n'
        result += f'Total Capacity Taken: {total_capacity_all_software_components} / {total_capacity_all_hardware_components}\n'
        return result

    @staticmethod
    def system_split():
        hardwares = System.get_hardware()

        for current_hardware in hardwares:
            current_total_express_sofwares = 0
            current_total_light_softwares = 0
            total_memory_all_software_components = 0
            total_capacity_all_software_components = 0
            software_names = []

            for software in current_hardware.software_components:
                total_memory_all_software_components += software.memory_consumption
                total_capacity_all_software_components += software.capacity_consumption
                software_names.append(software.name)

                if software.software_type == 'Express':
                    current_total_express_sofwares += 1
                elif software.software_type == 'Light':
                    current_total_light_softwares += 1

            if not software_names:
                software_names = None
            else:
                software_names = ', '.join(software_names)

            result = f'Hardware Component - {current_hardware.name}\n'
            result += f'Express Software Components: {current_total_express_sofwares}\n'
            result += f'Light Software Components: {current_total_light_softwares}\n'
            result += f'Memory Usage: {total_memory_all_software_components} / {current_hardware.memory}\n'
            result += f'Capacity Usage: {total_capacity_all_software_components} / {current_hardware.capacity}\n'
            result += f'Type: {current_hardware.hardware_type}\n'
            result += f'Software Components: {software_names}'
