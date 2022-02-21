# courses = {}
#
# while True:
#     command = input()
#     if command == 'end':
#         break
#
#     command_list = command.split(' : ')
#     course_name = command_list[0]
#     student_name = command_list[1]
#
#     if course_name not in courses:
#         courses.update({course_name: [student_name]})
#     else:
#         courses[course_name].append(student_name)
#
# courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))
# for element in courses:
#     mini_list = courses[element]
#     print(f'{element}: {len(mini_list)}')
#     mini_list.sort()
#     for name in mini_list:
#         print(f'-- {name}')

courses_users = {}
while True:
    command = input()
    if command == 'end':
        break

    if command.split(' : ')[0] not in courses_users:
        courses_users.update({command.split(' : ')[0]: [command.split(' : ')[1]]})
    else:
        courses_users[command.split(' : ')[0]].append(command.split(' : ')[1])

for key, value in dict(sorted(courses_users.items(), key=lambda x: (-len(x[1]), x[0]))).items():
    print(f"{key}: {len(value)}")
    for student in value:
        print(f"-- {student}")
