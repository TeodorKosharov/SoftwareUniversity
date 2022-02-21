from collections import deque

materials_stack = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

first_pair = {'Doll': 0, 'Wooden train': 0}
second_pair = {'Teddy bear': 0, 'Bicycle': 0}

while materials_stack and magic_level:
    current_material = materials_stack[-1]
    current_magic = magic_level[0]

    if current_material == 0:
        materials_stack.pop()

    if current_magic == 0:
        magic_level.popleft()

    total_magic_level = current_magic * current_material

    if total_magic_level == 150:
        first_pair['Doll'] += 1
        materials_stack.pop()
        magic_level.popleft()

    elif total_magic_level == 250:
        first_pair['Wooden train'] += 1
        materials_stack.pop()
        magic_level.popleft()

    elif total_magic_level == 300:
        second_pair['Teddy bear'] += 1
        materials_stack.pop()
        magic_level.popleft()

    elif total_magic_level == 400:
        second_pair['Bicycle'] += 1
        materials_stack.pop()
        magic_level.popleft()

    elif total_magic_level < 0:
        magic_level.popleft()
        materials_stack[-1] += current_magic

    elif total_magic_level > 0:
        magic_level.popleft()
        materials_stack[-1] += 15

first_pair_comprehension = [x for x in first_pair.values() if x > 0]
second_pair_comprehension = [x for x in second_pair.values() if x > 0]

if len(first_pair_comprehension) == 2 or len(second_pair_comprehension) == 2:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_stack:
    print(f'Materials left: {", ".join([str(x) for x in reversed(materials_stack)])}')

if magic_level:
    print(f'Magic left: {", ".join([str(x) for x in magic_level])}')

first_pair.update(second_pair)
all_crafted_presents_sorted = dict(sorted(first_pair.items(), key=lambda x: x[0]))
all_crafted_presents_filtered = {k: v for k, v in all_crafted_presents_sorted.items() if v >= 1}
for toy, amount in all_crafted_presents_filtered.items():
    print(f'{toy}: {amount}')
