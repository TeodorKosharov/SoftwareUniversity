intersections = []

for _ in range(int(input())):
    case = input().split('-')
    first_case = case[0].split(',')
    second_case = case[1].split(',')

    first_set = set()
    second_set = set()

    for num1 in range(int(first_case[0]), int(first_case[1]) + 1):
        first_set.add(num1)

    for num2 in range(int(second_case[0]), int(second_case[1]) + 1):
        second_set.add(num2)

    intersections.append(first_set & second_set)

sorted_intersections = sorted(intersections, key=lambda x: -len(x))
max_intersection = sorted_intersections[0]

print(f'Longest intersection is {list(max_intersection)} with length {len(max_intersection)}')
