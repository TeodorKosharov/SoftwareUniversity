def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    elements = 3

    for row in range(2, n):
        new_row = []

        for el in range(elements):
            if el - 1 < 0:
                new_row.append(1)
                continue
            if el >= len(triangle[-1]):
                new_row.append(1)
                break

            value = triangle[row - 1][el - 1] + triangle[row - 1][el]
            new_row.append(value)

        triangle.append(new_row)
        elements += 1

    return triangle


a = get_magic_triangle(5)
for row in a:
    print(*row)
