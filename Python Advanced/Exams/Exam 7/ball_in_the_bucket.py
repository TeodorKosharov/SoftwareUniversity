def is_inside(r, c):
    return 0 <= r < 6 and 0 <= c < 6


board = []
buckets_coordinates = []
points = 0

for row in range(6):
    current_row = input().split()
    board.append(current_row)

for turn in range(3):
    shot = eval(input())
    shot_row, shot_col = shot

    if is_inside(*shot):

        if board[shot_row][shot_col] == 'B' and (shot_row, shot_col) not in buckets_coordinates:
            buckets_coordinates.append((shot_row, shot_col))

            for row in range(0, 6):
                if board[row][shot_col] != 'B':
                    points += int(board[row][shot_col])

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
