from collections import deque


def check_result(res):
    if 100 <= res <= 199:
        gifts['Gemstone'] += 1
    elif 200 <= res <= 299:
        gifts['Porcelain Sculpture'] += 1
    elif 300 <= res <= 399:
        gifts['Gold'] += 1
    elif 400 <= res <= 499:
        gifts['Diamond Jewellery'] += 1


materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

gifts = {'Gemstone': 0,
         'Porcelain Sculpture': 0,
         'Gold': 0,
         'Diamond Jewellery': 0}

succeeded = False

while materials and magic_levels:
    current_material = materials.pop()
    current_magic = magic_levels.popleft()
    result = current_material + current_magic

    if 100 <= result <= 199:
        gifts['Gemstone'] += 1
    elif 200 <= result <= 299:
        gifts['Porcelain Sculpture'] += 1
    elif 300 <= result <= 399:
        gifts['Gold'] += 1
    elif 400 <= result <= 499:
        gifts['Diamond Jewellery'] += 1
    elif result < 100:
        if result % 2 == 0:
            check_result((current_material * 2) + (current_magic * 3))
        elif result % 2 != 0:
            check_result((current_material * 2) + (current_magic * 2))

    elif result > 499:
        check_result((current_material // 2) + (current_magic // 2))

    if (gifts['Gemstone'] >= 1 and gifts['Porcelain Sculpture'] >= 1) or (
            gifts['Gold'] >= 1 and gifts['Diamond Jewellery'] >= 1):
        succeeded = True

if succeeded:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

for gift, amount in sorted(gifts.items(), key=lambda x: x[0]):
    if amount >= 1:
        print(f"{gift}: {amount}")
