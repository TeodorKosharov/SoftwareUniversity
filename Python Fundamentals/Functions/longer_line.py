from math import floor as f


def longer_line(a1, b1, a2, b2, a3, b3, a4, b4):
    c1 = a1 ** 2 + b1 ** 2
    c2 = a2 ** 2 + b2 ** 2
    first_line = c1 + c2

    c3 = a3 ** 2 + b3 ** 2
    c4 = a4 ** 2 + b4 ** 2
    second_line = c3 + c4

    if first_line > second_line:
        if c2 > c1:
            print(f'({f(a1)}, {f(b1)})({f(a2)}, {f(b2)})')
        elif c2 < c1:
            print(f'({f(a2)}, {f(b2)})({f(a1)}, {f(b1)})')
        else:
            print(f'({f(a1)}, {f(b1)})({f(a2)}, {f(b2)})')

    elif first_line < second_line:
        if c3 > c4:
            print(f'({f(a4)}, {f(b4)})({f(a3)}, {f(b3)})')
        elif c3 < c4:
            print(f'({f(a3)}, {f(b3)})({f(a4)}, {f(b4)})')
        else:
            print(f'({f(a3)}, {f(b3)})({f(a4)}, {f(b4)})')
    elif first_line == second_line:
        print(f'({f(a1)}, {f(b1)})({f(a2)}, {f(b2)})')


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
