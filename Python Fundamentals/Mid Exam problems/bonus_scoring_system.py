from math import ceil

students = int(input())
lectures = int(input())
bonus = int(input())

max_points = 0
max_student_lecture = 0

for student in range(students):

    attendances = int(input())
    total_bonus = (attendances / lectures) * (5 + bonus)

    if total_bonus >= max_points:
        max_points = total_bonus
        max_student_lecture = attendances

print(f"Max Bonus: {ceil(max_points)}.")
print(f"The student has attended {max_student_lecture} lectures.")
