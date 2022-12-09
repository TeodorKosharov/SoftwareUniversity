animals = input()

animals_list = animals.split(', ')

wolf_position = animals_list.index("wolf")
wolf_position += 1

remaining_sheeps = len(animals_list) - wolf_position

if animals_list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {remaining_sheeps}! You are about to be eaten by a wolf!")

