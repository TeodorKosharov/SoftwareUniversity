def smallest_number(a, b, c):
    if a < b and a < c:
        return a

    elif b < a and b < c:
        return b

    elif c < a and c < b:
        return c


result = smallest_number(int(input()), int(input()), int(input()))
print(result)
