users = {}
submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break

    if 'banned' in command:
        command_list = command.split('-')
        users.pop(command_list[0])
        continue

    username, language, points = command_list = command.split('-')
    points = int(points)

    if username not in users:
        users[username] = [points]
    elif username in users:
        users[username].append(points)

    if language not in submissions:
        submissions[language] = 1
    elif language in submissions:
        submissions[language] += 1

users = dict(sorted(users.items(), key=lambda x: (-max(x[1]), x[0])))
submissions = dict(sorted(submissions.items(), key=lambda x: (-x[1], x[0])))

print('Results:')
for name, points in users.items():
    print(f'{name} | {max(points)}')

print('Submissions:')
for lang, subs in submissions.items():
    print(f'{lang} - {subs}')
