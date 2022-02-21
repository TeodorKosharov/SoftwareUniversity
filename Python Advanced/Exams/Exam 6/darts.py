def get_corresponding_nums(check_row, check_col, hit_letter):
    score = int(dartboard[check_row][0])
    score += int(dartboard[check_row][6])
    score += int(dartboard[0][check_col])
    score += int(dartboard[6][check_col])

    if hit_letter == 'D':
        return score * 2
    return score * 3


first_player, second_player = input().split(', ')

dartboard = []
scores = {first_player: 501, second_player: 501}
throws = {first_player: 0, second_player: 0}
player = 1

for row in range(7):
    dartboard.append(input().split())

while True:

    current_player = first_player if player % 2 == 1 else second_player

    player += 1
    throws[current_player] += 1
    hit_row, hit_col = eval(input())

    if hit_row >= 7 or hit_row < 0 or hit_col >= 7 or hit_col < 0:
        continue

    elif dartboard[hit_row][hit_col].isdigit():
        scores[current_player] -= int(dartboard[hit_row][hit_col])

    elif dartboard[hit_row][hit_col] == 'D':
        scores[current_player] -= get_corresponding_nums(hit_row, hit_col, 'D')

    elif dartboard[hit_row][hit_col] == 'T':
        scores[current_player] -= get_corresponding_nums(hit_row, hit_col, 'T')

    elif dartboard[hit_row][hit_col] == 'B':
        scores[current_player] = 0

    if scores[current_player] <= 0:
        break

print(f'{current_player} won the game with {throws[current_player]} throws!')
