fires = input()
water = int(input())

fires_list = fires.split('#')

is_cell_valid = False

total_effort = 0
total_fire = 0

cells_list = []

for cell in fires_list:

    current_cell = cell.split(' = ')
    fire_type = current_cell[0]
    cell_value = int(current_cell[1])

    if cell_value > water:
        continue

    if fire_type == 'High' and 81 <= cell_value <= 125:
        is_cell_valid = True

    elif fire_type == "Medium" and 51 <= cell_value <= 80:
        is_cell_valid = True

    elif fire_type == "Low" and 1 <= cell_value <= 50:
        is_cell_valid = True

    else:
        is_cell_valid = False

    if is_cell_valid:

        water -= cell_value
        total_effort += 0.25 * cell_value
        total_fire += cell_value
        cells_list.append(cell_value)

print('Cells:')

for element in cells_list:
    print(f" - {element}")

print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire:.0f}')
