# junk = {}
# legs = {'shards': 0, 'fragments': 0, 'motes': 0}
# flag = False
#
# while True:
#     inp = input().split(' ')
#
#     quantity = [int(x) for x in inp if x.isdigit()]
#     materials = [y.lower() for y in inp if not y.isdigit()]
#
#     materials_list = list(zip(materials, quantity))
#
#     for element in materials_list:
#         material = element[0]
#         quantity = element[1]
#
#         if material == 'shards':
#             legs[material] += quantity
#             if legs[material] >= 250:
#                 item = "Shadowmourne"
#                 legs[material] -= 250
#                 flag = True
#                 break
#
#         elif material == 'fragments':
#             legs[material] += quantity
#             if legs[material] >= 250:
#                 item = "Valanyr"
#                 legs[material] -= 250
#                 flag = True
#                 break
#
#         elif material == 'motes':
#             legs[material] += quantity
#             if legs[material] >= 250:
#                 item = "Dragonwrath"
#                 legs[material] -= 250
#                 flag = True
#                 break
#
#         else:
#             if material not in junk:
#                 junk[material] = quantity
#             else:
#                 junk[material] += quantity
#
#     if flag:
#         break
#
# print(f"{item} obtained!")
# sorted_legs = dict(sorted(legs.items(), key=lambda x: (-x[1], x[0])))
# for element in sorted_legs:
#     print(f'{element}: {sorted_legs[element]}')
#
# sorted_junks = dict(sorted(junk.items(), key=lambda x: x[0]))
# for element in sorted_junks:
#     print(f'{element}: {sorted_junks[element]}')


def printing(materials_dict: dict, junk_dict: dict):
    materials_dict = dict(sorted(materials_dict.items(), key=lambda x: (-x[1], x[0])))
    junk_dict = dict(sorted(junk_dict.items(), key=lambda x: x[0]))

    for key, value in materials_dict.items():
        print(f"{key}: {value}")

    for key, value in junk_dict.items():
        print(f"{key}: {value}")


materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junks = {}

while True:
    inp = input().split()
    index = 0

    for complect in range(len(inp) // 2):
        quantity = int(inp[index])
        index += 1
        material = inp[index].lower()
        index += 1

        if material in materials:
            materials[material] += quantity
        else:
            if material not in junks:
                junks.update({material: quantity})
            else:
                junks[material] += quantity

        if materials['shards'] >= 250:
            materials['shards'] -= 250
            print(f"Shadowmourne obtained!")
            printing(materials, junks)
            exit()
        elif materials['fragments'] >= 250:
            materials['fragments'] -= 250
            print(f"Valanyr obtained!")
            printing(materials, junks)
            exit()
        elif materials['motes'] >= 250:
            materials['motes'] -= 250
            print(f"Dragonwrath obtained!")
            printing(materials, junks)
            exit()
