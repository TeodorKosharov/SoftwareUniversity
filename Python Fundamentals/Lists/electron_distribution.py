number_of_electrons = int(input())

electrons_list = []
current_position = 1

while True:

    max_electrons_per_shield = 2 * current_position ** 2

    if max_electrons_per_shield >= number_of_electrons:
        max_electrons_per_shield = number_of_electrons
        electrons_list.append(max_electrons_per_shield)
        break

    electrons_list.append(max_electrons_per_shield)
    number_of_electrons -= max_electrons_per_shield
    current_position += 1

print(electrons_list)
