houses = [int(num) for num in input().split('@')]
jump_index = 0
while True:
    command = input()

    if command == 'Love!':
        break

    command_list = command.split()
    current_jump = int(command_list[1])
    jump_index += current_jump

    if jump_index <= len(houses) - 1:
        if houses[jump_index] > 0:
            houses[jump_index] -= 2
            if houses[jump_index] == 0:
                print(f"Place {jump_index} has Valentine's day.")
        elif houses[jump_index] == 0:
            print(f"Place {jump_index} already had Valentine's day.")
    else:
        jump_index = 0
        if houses[jump_index] > 0:
            houses[jump_index] -= 2
            if houses[jump_index] == 0:
                print(f"Place {jump_index} has Valentine's day.")
        elif houses[jump_index] == 0:
            print(f"Place {jump_index} already had Valentine's day.")

print(f"Cupid's last position was {jump_index}.")

completed_houses = houses.count(0)
total_houses = len(houses)

if completed_houses == total_houses:
    print("Mission was successful.")
elif completed_houses < total_houses:
    print(f"Cupid has failed {total_houses - completed_houses} places.")
