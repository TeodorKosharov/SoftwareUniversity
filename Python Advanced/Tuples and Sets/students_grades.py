students = {}

for _ in range(int(input())):
    student_data = input().split()
    if student_data[0] not in students:
        students[student_data[0]] = [float(student_data[1])]
    else:
        students[student_data[0]].append(float(student_data[1]))

for data in students.items():
    print(f'{data[0]} -> {" ".join([f"{x:.2f}" for x in data[1]])} (avg: {sum(data[1]) / len(data[1]):.2f})')
