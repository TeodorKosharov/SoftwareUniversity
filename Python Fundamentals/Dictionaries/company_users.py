# users = {}
# submissions = {}
#
# while True:
#     inp = input()
#     if inp == 'exam finished':
#         break
#
#     commands = inp.split('-')
#     if len(commands) == 3:
#         username, language, points = commands
#         points = int(points)
#         if username not in users:
#             users[username] = [points]
#         elif username in users:
#             users[username].append(points)
#
#         if language not in submissions:
#             submissions[language] = [points]
#         elif language in submissions:
#             submissions[language].append(points)
#
#     elif len(commands) == 2:
#         username = commands[0]
#         if username in users:
#             users.pop(username)
#
# users = dict(sorted(users.items(), key=lambda x: (-max(x[1]), x[0])))
# submissions = dict(sorted(submissions.items(), key=lambda x: (-len(x[1]), x[0])))
#
# print('Results:')
# for user, points in users.items():
#     print(f'{user} | {max(points)}')
#
# print('Submissions:')
# for lang, subs in submissions.items():
#     print(f'{lang} - {len(subs)}')


company_users = {}
while True:
    command = input()
    if command == 'End':
        break

    if command.split(' -> ')[0] not in company_users:
        company_users.update({command.split(' -> ')[0]: [command.split(' -> ')[1]]})
    else:
        if command.split(' -> ')[1] not in company_users[command.split(' -> ')[0]]:
            company_users[command.split(' -> ')[0]].append(command.split(' -> ')[1])

for key, value in dict(sorted(company_users.items(), key=lambda x: x[0])).items():
    print(key)
    for user_id in value:
        print(f'-- {user_id}')
