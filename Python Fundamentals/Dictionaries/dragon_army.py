def stat_checker(dmg, health, arm):
    if dmg == 'null':
        dmg = 45
    else:
        dmg = int(dmg)

    if health == 'null':
        health = 250
    else:
        health = int(health)

    if arm == 'null':
        arm = 10
    else:
        arm = int(arm)

    return [dmg, health, arm]


def avg_dmg(dragons_dict: dict):
    dmg_by_type = []
    for dragon_type, dragon_names in dragons_dict.items():
        curr_dmg = 0
        for name in dragon_names:
            curr_dmg += dragon_names[name][0]
        average = curr_dmg / len(dragon_names.keys())
        dmg_by_type.append(average)
    return dmg_by_type


def avg_hp(dragons_dict: dict):
    hp_by_type = []
    for dragon_type, dragon_names in dragons_dict.items():
        curr_hp = 0
        for name in dragon_names:
            curr_hp += dragon_names[name][1]
        average = curr_hp / len(dragon_names.keys())
        hp_by_type.append(average)
    return hp_by_type


def avg_arm(dragons_dict: dict):
    arm_by_type = []
    for dragon_type, dragon_names in dragons_dict.items():
        curr_arm = 0
        for name in dragon_names:
            curr_arm += dragon_names[name][2]
        average = curr_arm / len(dragon_names.keys())
        arm_by_type.append(average)
    return arm_by_type


n = int(input())
dragons = {}

for i in range(n):

    inp = input().split(' ')
    dragon_type, dragon_name, damage, hp, armor = inp
    current_stats = stat_checker(damage, hp, armor)

    if dragon_type not in dragons:
        dragons.update({dragon_type: {dragon_name: current_stats}})
    else:
        if dragon_name in dragons[dragon_type]:
            dragons[dragon_type][dragon_name] = current_stats
        else:
            dragons[dragon_type].update({dragon_name: current_stats})

damages = avg_dmg(dragons)
hps = avg_hp(dragons)
armors = avg_arm(dragons)

stat_index = 0

for current_type, all_dragons in dragons.items():
    all_dragons = dict(sorted(all_dragons.items(), key=lambda x: x[0]))
    print(f'{current_type}::({damages[stat_index]:.2f}/{hps[stat_index]:.2f}/{armors[stat_index]:.2f})')
    for curr_dragon, stats in all_dragons.items():
        print(f"-{curr_dragon} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}")
    stat_index += 1
