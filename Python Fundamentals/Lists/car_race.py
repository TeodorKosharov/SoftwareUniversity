sequence = list(map(int, input().split(' ')))

middle_index = (len(sequence) - 1) // 2

left_side = sequence[:middle_index]
right_side = sequence[middle_index + 1:]
right_side.reverse()

left_time = 0
right_time = 0

for index in range(len(left_side)):
    if left_side[index] == 0:
        left_time *= 0.8
    elif left_side[index] > 0:
        left_time += left_side[index]

    if right_side[index] == 0:
        right_time *= 0.8
    elif right_side[index] > 0:
        right_time += right_side[index]

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
elif right_time < left_time:
    print(f"The winner is right with total time: {right_time:.1f}")
