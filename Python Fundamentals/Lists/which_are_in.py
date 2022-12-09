first_inp = input().split(', ')
second_inp = input().split(', ')

final_list = []

for first_list_index in range(len(first_inp)):
    for second_list_index in range(len(second_inp)):
        if first_inp[first_list_index] in second_inp[second_list_index]:
            final_list.append(first_inp[first_list_index])
            break

print(final_list)
