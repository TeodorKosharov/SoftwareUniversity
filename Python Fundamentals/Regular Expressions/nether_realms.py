import re


def damage_definer(dmg_value: str):
    if '.' in dmg_value:
        res_dmg = float(dmg_value)
    else:
        res_dmg = int(dmg_value)
    return res_dmg


def dmg_sings_counter(input_element: str, all_dmg):
    multipliers = input_element.count('*')
    dividers = input_element.count('/')
    for multiplier in range(multipliers):
        all_dmg *= 2
    for divider in range(dividers):
        all_dmg /= 2
    return all_dmg


inp = re.split(", *", input())

health_pattern = r'[^\d+\+\-\*\/\.]'
damage_pattern = r'[\+|\-]?\d+(\.\d+)?'
names_data = {}

for element in inp:
    element = element.strip()
    hp_match = re.finditer(health_pattern, element)
    dmg_match = re.finditer(damage_pattern, element)

    health = ''
    health_total_ascii_value = 0
    total_damage = 0

    for match in hp_match:
        health += match.group()

    for char in health:
        health_total_ascii_value += ord(char)

    for match in dmg_match:
        dmg = match.group()
        current_dmg = damage_definer(dmg)
        total_damage += current_dmg

    total_damage = dmg_sings_counter(element, total_damage)
    names_data[element] = [health_total_ascii_value, total_damage]

names_data = dict(sorted(names_data.items(), key=lambda x: x[0]))

for name, stats in names_data.items():
    print(f'{name} - {stats[0]} health, {stats[1]:.2f} damage')
