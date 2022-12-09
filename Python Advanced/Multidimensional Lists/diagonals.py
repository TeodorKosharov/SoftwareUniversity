primary_diagonal = []
secondary_diagonal = []

for index in range(int(input())):
    current_row = list(map(int, input().split(', ')))
    primary_diagonal.append(current_row[index])
    secondary_diagonal.append(current_row[-(index + 1)])

print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}')
