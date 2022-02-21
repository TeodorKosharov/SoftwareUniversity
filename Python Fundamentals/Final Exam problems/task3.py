animals = {}
areas = {}

while True:
    command = input()
    if command == "EndDay":
        break
    command_list = command.split(':')
    if command_list[0] == 'Add':
        animal_data = command_list[1].split('-')
        animal_name, needed_food, area = animal_data
        needed_food = int(needed_food)

        if animal_name not in animals:
            animals[animal_name] = needed_food
        elif animal_name in animals:
            animals[animal_name] += needed_food

        if area not in areas:
            areas[area] = [animal_name]
        elif area in areas:
            if animal_name not in areas[area]:
                areas[area].append(animal_name)

    elif command_list[0] == 'Feed':
        animal_data = command_list[1].split('-')
        animal_name = animal_data[0]
        food = int(animal_data[1])

        if animal_name in animals:
            animals[animal_name] -= food
            if animals[animal_name] <= 0:
                print(f"{animal_name.strip()} was successfully fed")
                animals.pop(animal_name)

                for curr_area in areas:
                    if animal_name in areas[curr_area]:
                        areas[curr_area].remove(animal_name)

animals = dict(sorted(animals.items(), key=lambda x: (-x[1], x[0])))
areas = dict(sorted(areas.items(), key=lambda x: (-len(x[1]), x[0])))

print("Animals:")
for name, food_quantity in animals.items():
    print(f' {name.strip()} -> {food_quantity}g')

print("Areas with hungry animals:")

for area_name, hungry_animals in areas.items():
    if len(hungry_animals) > 0:
        print(f" {area_name}: {len(hungry_animals)}")
