passwords = {}
participants = {}

while True:
    inp = input()
    if inp == 'end of contests':
        break

    commands = inp.split(':')
    contest, password = commands
    passwords[contest] = password

while True:
    inp = input()
    if inp == "end of submissions":
        break

    commands = inp.split('=>')
    contest, password, username, points = commands
    points = int(points)
    if contest in passwords and password == passwords[contest]:
        if username not in participants:
            participants[username] = {contest: points}
        elif username in participants:
            if contest not in participants[username]:
                participants[username][contest] = points
            elif contest in participants[username] and points > participants[username][contest]:
                participants[username][contest] = points


participants = dict(sorted(participants.items(), key=lambda x: x[0]))
total_points = {}

for key, value in participants.items():
    curr_points = 0
    for pp in value.values():
        curr_points += pp
    total_points[key] = curr_points

total_points = dict(sorted(total_points.items(),key=lambda x: -x[1]))

for key, value in total_points.items():
    print(f"Best candidate is {key} with total {value} points.")
    break

print('Ranking:')
for key, value in participants.items():
    print(key)
    value = dict(sorted(value.items(), key=lambda x: -x[1]))
    for mini_key, mini_value in value.items():
        print(f'#  {mini_key} -> {mini_value}')
