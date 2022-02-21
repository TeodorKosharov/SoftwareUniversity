def tribonacci_sequence(x):
    values = [1]

    for i in range(x):
        if i == 0:
            print(values[i], end=' ')
            values.append(1)
        elif i == 1:
            print(values[i], end=' ')
        elif i == 2:
            print(values[i - 2] + values[i - 1], end=' ')
            values.append(values[i - 2] + values[i - 1])
        else:
            print(values[i - 3] + values[i - 2] + values[i - 1], end=' ')
            values.append(values[i - 3] + values[i - 2] + values[i - 1])


n = int(input())
tribonacci_sequence(n)
