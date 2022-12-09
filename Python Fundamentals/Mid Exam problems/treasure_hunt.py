initial_loot = input().split('|')

while True:
    command = input()
    if command == "Yohoho!":
        break
    command_list = command.split()
    if command_list[0] == 'Loot':
        for loot_item in command_list[1:]:
            if loot_item not in initial_loot:
                initial_loot.insert(0, loot_item)

    elif command_list[0] == 'Drop':
        if 0 <= int(command_list[1]) <= len(initial_loot) - 1:
            initial_loot.append(initial_loot.pop(int(command_list[1])))

    elif command_list[0] == 'Steal':
        stolen_items = []
        for stolen_item in range(int(command_list[1])):
            stolen_items.append(initial_loot.pop(-1))
            if len(initial_loot) == 0:
                break
        stolen_items.reverse()
        print(', '.join(stolen_items))

if initial_loot:
    items_total_lengths = sum([len(x) for x in initial_loot])
    print(f"Average treasure gain: {items_total_lengths / len(initial_loot):.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
