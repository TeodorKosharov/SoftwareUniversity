quantity = int(input())
days = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

total_spirit = 0
suma = 0

is_last_day = False

for day in range(1, days + 1):

    if day % 11 == 0:
        quantity += 2
        is_last_day = False

    if day % 2 == 0:
        suma += ornament_set_price * quantity
        total_spirit += 5

    if day % 3 == 0:
        suma += (tree_skirt_price * quantity) + (tree_garlands_price * quantity)
        total_spirit += 13

    if day % 5 == 0:
        suma += tree_lights_price * quantity
        total_spirit += 17

        if day % 3 == 0:
            total_spirit += 30

    if day % 10 == 0:
        total_spirit -= 20
        suma += 23
        is_last_day = True

if is_last_day:
    total_spirit -= 30

print(f"Total cost: {suma}")
print(f"Total spirit: {total_spirit}")
