integers = list(map(int, input().split('@')))
current_index = 0

while True:
    command = input()
    if command == 'Love!':
        break

    given_index = int(command.split()[1])
    current_index += given_index
    if current_index > len(integers) - 1:
        current_index = 0

    if integers[current_index] != 0:
        integers[current_index] -= 2
        if integers[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")
    else:
        print(f"Place {current_index} already had Valentine's day.")

print(f"Cupid's last position was {current_index}.")

if integers.count(0) == len(integers):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len([x for x in integers if x != 0])} places.")
