sequence = list(map(int, input().split()))
average = sum(sequence) / len(sequence)
sequence.sort(reverse=True)

result_list = []

for element in sequence:
    if element > average:
        result_list.append(element)
        if len(result_list) == 5:
            break

if result_list:
    print(' '.join(list(map(str, result_list))))
else:
    print('No')
