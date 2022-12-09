all_lines = [input().split(), input().split(), input().split()]

all_rows = [
    [all_lines[0][0], all_lines[1][0], all_lines[2][0]],
    [all_lines[0][1], all_lines[1][1], all_lines[2][1]],
    [all_lines[0][2], all_lines[1][2], all_lines[2][2]]
]

all_diagonals = [
    [all_lines[0][0], all_lines[1][1], all_lines[2][2]],
    [all_lines[0][2], all_lines[1][1], all_lines[2][0]]
]

for line in all_lines:
    if line.count('1') == len(line):
        print("First player won")
        exit()
    elif line.count('2') == len(line):
        print("Second player won")
        exit()

for row in all_rows:
    if row.count('1') == len(row):
        print("First player won")
        exit()
    elif row.count('2') == len(row):
        print("Second player won")
        exit()

for diagonal in all_diagonals:
    if diagonal.count('1') == len(diagonal):
        print("First player won")
        exit()
    elif diagonal.count('2') == len(diagonal):
        print("Second player won")
        exit()

print('Draw!')
