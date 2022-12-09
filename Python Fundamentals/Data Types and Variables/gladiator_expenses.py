lost_fights_coint = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
is_helmet_broken = False
is_sword_broken = False
broken_shield_counter = 0

for lose in range(1, lost_fights_coint + 1):

    if lose % 2 == 0:
        expenses += helmet_price
        is_helmet_broken = True

    if lose % 3 == 0:
        expenses += sword_price
        is_sword_broken = True

    if is_sword_broken and is_helmet_broken:
        broken_shield_counter += 1
        expenses += shield_price

    if broken_shield_counter % 2 == 0 and broken_shield_counter != 0:
        expenses += armor_price
        broken_shield_counter = 0

    is_helmet_broken = False
    is_sword_broken = False

print(f"Gladiator expenses: {expenses:.2f} aureus")
