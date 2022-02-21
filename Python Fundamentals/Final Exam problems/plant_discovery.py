n = int(input())

plants = {}

for _ in range(n):
    inp = input().split('<->')
    plant, rarity = inp
    rarity = int(rarity)
    plants[plant] = {'Rarity': rarity, 'Rating': []}

while True:
    command = input()
    if command == "Exhibition":
        break
    command_list = command.split(':')
    action = command_list[0]

    if action == 'Rate':
        plant, rating = command_list[1].split(' - ')
        plant = plant.strip()
        rating = int(rating)
        if plant in plants:
            plants[plant]['Rating'].append(rating)
        elif plant not in plants:
            print("error")

    elif action == 'Update':
        plant, new_rarity = command_list[1].split(' - ')
        plant = plant.strip()
        new_rarity = int(new_rarity)
        if plant in plants:
            plants[plant]['Rarity'] = new_rarity
        elif plant not in plants:
            print("error")

    elif action == 'Reset':
        plant = command_list[1].strip()
        if plant in plants:
            plants[plant]['Rating'] = []
        elif plant not in plants:
            print("error")

for curr_plant in plants:
    if len(plants[curr_plant]['Rating']) == 0:
        plants[curr_plant]['Rating'] = 0
    else:
        plants[curr_plant]['Rating'] = sum(plants[curr_plant]['Rating']) / len(plants[curr_plant]['Rating'])

plants = dict(sorted(plants.items(), key=lambda x: (-x[1]['Rarity'], -x[1]['Rating'])))

print('Plants for the exhibition:')
for k, v in plants.items():
    print(f'- {k}; Rarity: {v["Rarity"]}; Rating: {v["Rating"]:.2f}')
