rows, cols = [int(x) for x in input().split()]
snake = input()

snake_index = 0
matrix = []

for row in range(rows):
    res = ''
    for column in range(cols):
        res += snake[snake_index]
        snake_index += 1
        if snake_index == len(snake):
            snake_index = 0

    if row % 2 == 1 and row > 0:  # on every odd row we should reverse the result string
        matrix.append(res[::-1])
    else:
        matrix.append(res)

for row in matrix:
    print(row)
