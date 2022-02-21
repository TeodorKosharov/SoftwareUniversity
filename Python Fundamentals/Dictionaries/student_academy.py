# n = int(input())
#
# students = {}
#
# for i in range(n):
#     student_name = input()
#     grade = float(input())
#
#     if student_name not in students:
#         students.update({student_name: [grade]})
#     else:
#         students[student_name].append(grade)
#
# for current_student_name in students:
#     mini_list = students[current_student_name]
#     average_grade = sum(mini_list) / len(mini_list)
#     students[current_student_name] = average_grade
#
# students = list(students.items())
# filtered_students = {k: v for (k, v) in students if v >= 4.50}
#
# filtered_students = dict(sorted(filtered_students.items(), key=lambda x: -x[1]))
# for element in filtered_students:
#     print(f'{element} -> {filtered_students[element]:.2f}')


students = {}
for _ in range(int(input())):
    name = input()
    score = float(input())

    if name not in students:
        students[name] = [score]
    else:
        students[name].append(score)

students = {k: (sum(v) / len(v)) for k, v in students.items() if sum(v) / len(v) >= 4.50}
for key, value in dict(sorted(students.items(), key=lambda x: -x[1])).items():
    print(f"{key} -> {value:.2f}")
