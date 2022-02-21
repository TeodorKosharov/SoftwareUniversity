# students = {}
#
# while True:
#     command = input()
#
#     if ':' not in command:
#         break
#
#     command_list = command.split(':')
#     key = command_list[0]
#     value = {command_list[2]: command_list[1]}
#     students[key] = value
#
# course = command
# if '_' in course:
#     course = course.replace('_', ' ')
#
# for key, mini_dict in students.items():
#     if course in mini_dict.keys():
#         print(f'{key} - {mini_dict[course]}')

students = {}
while True:
    inp = input().split(':')
    if len(inp) < 3:
        break

    students.update({inp[1]: [inp[0], inp[2]]})

inp = inp[0].replace('_', ' ')

for student_id, student_data in students.items():
    if inp == student_data[1]:
        print(f"{student_data[0]} - {student_id}")
