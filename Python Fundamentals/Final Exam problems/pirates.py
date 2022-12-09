crew = {}

while True:
    inp = input()
    if inp == 'Sail':
        break
    inp_list = inp.split('||')
    city = inp_list[0]
    population = int(inp_list[1])
    gold = int(inp_list[2])

    if city not in crew:
        crew[city] = [population, gold]
    elif city in crew:
        crew[city][0] += population
        crew[city][1] += gold

while True:
    command = input()
    if command == 'End':
        break
    command_list = command.split('=>')
    action = command_list[0]
    if action == 'Plunder':
        town = command_list[1]
        people = int(command_list[2])
        gold = int(command_list[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        crew[town][0] -= people
        crew[town][1] -= gold
        if crew[town][0] == 0 or crew[town][1] == 0:
            print(f"{town} has been wiped off the map!")
            crew.pop(town)

    elif action == 'Prosper':
        town = command_list[1]
        gold = int(command_list[2])
        if gold > 0:
            crew[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {crew[town][1]} gold.")
        elif gold < 0:
            print("Gold added cannot be a negative number!")

crew = dict(sorted(crew.items(), key=lambda x: (-x[1][1], x[0])))

print(f'Ahoy, Captain! There are {len(crew)} wealthy settlements to go to:')

for k, v in crew.items():
    print(f'{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg')
