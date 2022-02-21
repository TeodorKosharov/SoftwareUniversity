def get_side(dictionary, user):
    for key in dictionary:
        if dictionary[key] == user:
            return key


def is_there_force_user(dictionary, user):
    for users in dictionary.values():
        if user in users:
            return True
    return False


forces = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    if '|' in command:
        force_side, force_user = command.split(' | ')

        if force_side not in forces and not is_there_force_user(forces, force_user):
            forces.update({force_side: [force_user]})
        elif not is_there_force_user(forces, force_user):
            forces[force_side].append(force_user)

    elif ' -> ' in command:
        force_user, force_side = command.split(' -> ')

        if is_there_force_user(forces, force_user):
            for side in forces:
                if force_user in forces[side]:
                    forces[side].remove(force_user)

            if not is_there_force_user(forces, force_user) and force_side not in forces:
                forces[force_side] = [force_user]

            elif not is_there_force_user(forces, force_user):
                forces[force_side].append(force_user)

            print(f'{force_user} joins the {force_side} side!')

        elif not is_there_force_user(forces, force_user):
            if force_side not in forces:
                forces[force_side] = [force_user]
            else:
                forces[force_side].append(force_user)
            print(f'{force_user} joins the {force_side} side!')

forces = {k: v for (k, v) in forces.items() if len(v) >= 1}
forces = dict(sorted(forces.items(), key=lambda x: (-len(x[1]), x[0])))

for side, users in forces.items():
    print(f'Side: {side}, Members: {len(users)}')
    users.sort()
    for user in users:
        print(f'! {user}')
