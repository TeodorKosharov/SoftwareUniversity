sequence = list(map(int, input().split()))

while True:
    inp = input()
    if inp == 'End':
        print(f"Shot targets: {sequence.count(-1)} -> {' '.join(list(map(str, sequence)))}")
        break

    index = int(inp)
    if 0 <= index <= len(sequence) - 1:
        current_target_value = sequence[index]
        sequence[index] = -1

        for target in range(len(sequence)):
            if sequence[target] != -1:
                if sequence[target] > current_target_value:
                    sequence[target] -= current_target_value
                else:
                    sequence[target] += current_target_value
