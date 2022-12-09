import re


def get_name():
    x = re.findall(name_pattern, inp)
    x = ', '.join(x)
    x = x.replace(', ', '')
    return x


def get_distance():
    total_distance = 0
    y = re.findall(distance_pattern, inp)
    for num in y:
        total_distance += int(num)
    return total_distance


participants = input().split(', ')
participants_distances = {}

name_pattern = r'[A-Za-z]+'
distance_pattern = r'\d'

for participant in participants:
    participants_distances.update({participant: 0})

while True:
    inp = input()
    if inp == 'end of race':
        break

    current_name = get_name()
    current_distance = get_distance()

    if current_name in participants_distances:
        participants_distances[current_name] += current_distance

participants_distances = dict(sorted(participants_distances.items(), key=lambda x: -x[1]))

step = 1
for racer in participants_distances:
    if step == 1:
        z = '1st'
    elif step == 2:
        z = '2nd'
    elif step == 3:
        z = '3rd'
    else:
        break

    print(f'{z} place: {racer}')
    step += 1
