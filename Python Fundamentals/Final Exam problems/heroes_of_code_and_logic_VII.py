n = int(input())

heroes = {}

for _ in range(n):
    heroes_data = input().split(' ')
    hero_name = heroes_data[0]
    hit_points = int(heroes_data[1])
    mana_points = int(heroes_data[2])
    if hit_points <= 100 and mana_points <= 200:
        heroes.update({hero_name: [hit_points, mana_points]})

while True:
    command = input()
    if command == "End":
        break
    command_list = command.split(' - ')
    action = command_list[0]
    hero_name = command_list[1]

    if action == 'CastSpell':
        needed_mana = int(command_list[2])
        spell_name = command_list[3]

        if needed_mana <= heroes[hero_name][1]:
            heroes[hero_name][1] -= needed_mana
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == 'TakeDamage':
        damage = int(command_list[2])
        attacker = command_list[3]

        heroes[hero_name][0] -= damage
        if heroes[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            heroes.pop(hero_name)

    elif action == 'Recharge':
        amount = int(command_list[2])
        if heroes[hero_name][1] + amount > 200:
            recharged = 200 - heroes[hero_name][1]
            heroes[hero_name][1] = 200
        else:
            heroes[hero_name][1] += amount
            recharged = amount
        print(f"{hero_name} recharged for {recharged} MP!")

    elif action == 'Heal':
        amount = int(command_list[2])
        if heroes[hero_name][0] + amount > 100:
            healed = 100 - heroes[hero_name][0]
            heroes[hero_name][0] = 100
        else:
            heroes[hero_name][0] += amount
            healed = amount
        print(f"{hero_name} healed for {healed} HP!")

heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])))
for current_hero, hero_data in heroes.items():
    print(current_hero)
    print(f'  HP: {hero_data[0]}')
    print(f'  MP: {hero_data[1]}')
