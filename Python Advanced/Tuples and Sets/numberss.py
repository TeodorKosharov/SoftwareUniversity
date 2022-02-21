first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'Add':
        nums = [int(x) for x in command if x.isdigit()]
        if command[1] == 'First':
            for x in nums:
                first_sequence.add(x)
        else:
            for x in nums:
                second_sequence.add(x)

    elif command[0] == 'Remove':
        nums = [int(x) for x in command if x.isdigit()]
        if command[1] == 'First':
            for x in nums:
                first_sequence.discard(x)
        else:
            for x in nums:
                second_sequence.discard(x)

    else:
        print(bool(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence)))

first_sequence = sorted(first_sequence)
second_sequence = sorted(second_sequence)

print(*first_sequence, sep=', ')
print(*second_sequence, sep=', ')

