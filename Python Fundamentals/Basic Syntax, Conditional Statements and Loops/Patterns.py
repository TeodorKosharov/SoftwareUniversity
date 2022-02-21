value = int(input())

for i in range(1, value + 1):
    print()
    for k in range(1, i + 1):
        print("*", end="")

for a in range(value - 1, 0, -1):
    print()
    for b in range(1, a + 1):
        print("*", end="")
