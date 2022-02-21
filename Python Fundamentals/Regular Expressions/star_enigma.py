import re


def key_finder():
    key = 0
    for char in message.lower():
        if char in key_chars:
            key += 1
    return key


def formated_message(key):
    formatted_message = ''
    for char in message:
        formatted_message += chr(ord(char) - key)
    return formatted_message


n = int(input())
key_chars = ['s', 't', 'a', 'r']
pattern = r'@(?P<planet>[A-Za-z]+)([^@:\!>-]+)?:(?P<population>\d+)([^@:\!>-]+)?\!(?P<attack>[A|D])\!([^@:\!>-]+)?->(?P<count>\d+)([^@:\!>-]+)?'
attacked_planets = []
destroyed_planets = []

for line in range(n):
    message = input()
    key_value = key_finder()
    new_message = formated_message(key_value)
    matches = re.finditer(pattern, new_message)

    for match in matches:
        planet_name = match.group('planet')
        population = match.group('population')
        attack = match.group('attack')
        count = match.group('count')

        if planet_name and population and attack and count:
            planet_name = planet_name.replace('@', '')
            population = population.replace(':', '')
            attack = attack.replace('!', '')
            count = count.replace('->', '')

            if attack == 'A':
                attacked_planets.append(planet_name)
            elif attack == 'D':
                destroyed_planets.append(planet_name)

attacked_planets.sort()
destroyed_planets.sort()

print(f"Attacked planets: {len(attacked_planets)}")
for attacked_planet in attacked_planets:
    print(f"-> {attacked_planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for destroyed_planet in destroyed_planets:
    print(f"-> {destroyed_planet}")
