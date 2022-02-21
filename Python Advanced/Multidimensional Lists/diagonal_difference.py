primary_diagonal = []
secondary_diagonal = []

for index in range(int(input())):
    current_row = [int(x) for x in input().split()]
    primary_diagonal.append(current_row[index])
    secondary_diagonal.append(current_row[-(index + 1)])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
