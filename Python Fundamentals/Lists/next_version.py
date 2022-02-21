current_version = input().split('.')
current_version_ints = list(map(int, current_version))

is_increase_needed = False
for index in range(len(current_version_ints) - 1, -1, -1):
    if current_version_ints[index] + 1 < 10:
        current_version_ints[index] += 1
        break
    else:
        current_version_ints[index] = 0

dot = len(current_version_ints)

for index in range(len(current_version_ints)):
    print(current_version_ints[index], end='')
    dot -= 1

    if dot > 0:
        print('.', end='')
