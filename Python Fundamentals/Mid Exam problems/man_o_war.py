pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_hp = int(input())

while True:
    command = input()
    if command == "Retire":
        break
    command_list = command.split()

    if command_list[0] == 'Fire':
        if 0 <= int(command_list[1]) <= len(warship) - 1:
            warship[int(command_list[1])] -= int(command_list[2])
            if warship[int(command_list[1])] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()

    elif command_list[0] == 'Defend':
        if 0 <= int(command_list[1]) <= len(pirate_ship) - 1 and 0 <= int(command_list[2]) <= len(pirate_ship) - 1:
            for attacked_section in range(int(command_list[1]), int(command_list[2]) + 1):
                pirate_ship[attacked_section] -= int(command_list[3])
                if pirate_ship[attacked_section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif command_list[0] == 'Repair':
        if 0 <= int(command_list[1]) <= len(pirate_ship) - 1:
            pirate_ship[int(command_list[1])] += int(command_list[2])
            if pirate_ship[int(command_list[1])] > max_hp:
                pirate_ship[int(command_list[1])] = max_hp

    elif command_list[0] == 'Status':
        print(f"{len([x for x in pirate_ship if x < 0.20 * max_hp])} sections need repair.")

print(f'Pirate ship status: {sum(pirate_ship)}')
print(f'Warship status: {sum(warship)}')
