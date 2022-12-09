from math import floor


def center_point(a, b, a1, b1):
    c = pow(a, 2) + pow(b, 2)           # Теоремата на Питагор
    c1 = pow(a1, 2) + pow(b1, 2)

    if c < c1:
        print(f'({floor(a)}, {floor(b)})')
    elif c > c1:
        print(f'({floor(a1)}, {floor(b1)})')
    elif c == c1:
        print(f'({floor(a)}, {floor(b)})')


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

center_point(x1, y1, x2, y2)
