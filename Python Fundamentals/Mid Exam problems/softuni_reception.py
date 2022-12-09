first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())

total_employees = first_employee + second_employee + third_employee
hours = 0

while True:
    if students_count <= 0:
        break

    students_count -= total_employees
    hours += 1

    if hours % 4 == 0 and hours != 0:
        hours += 1

print(f"Time needed: {hours}h.")
