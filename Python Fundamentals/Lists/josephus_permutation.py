sequence = list(map(int, input().split(' ')))
k = int(input())

executed = []
start_index = -1

while len(sequence) > 0:
    for i in range(k):
        start_index += 1
        if start_index > len(sequence) - 1:
            start_index = 0

    executed.append(sequence.pop(start_index))
    start_index -= 1

print(f'[{",".join(list(map(str, executed)))}]')
