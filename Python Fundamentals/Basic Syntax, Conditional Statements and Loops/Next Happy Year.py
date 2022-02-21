year = int(input())

while True:

    year += 1
    year = str(year)
    condition = True

    for i in range(len(year)):
        symbol = year[i]

        if not condition:
            break

        for x in range(i + 1, len(year)):

            rest_symbol = year[x]

            if symbol == rest_symbol:
                condition = False
                break

    if condition:
        print(year)
        break

    year = int(year)