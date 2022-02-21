sequence = list(map(int, input().split()))
capacity = int(input())

suma = 0
racks = 0

while sequence:
    suma += sequence[-1]
    if suma < capacity:
        if len(sequence) == 1:
            racks += 1
        sequence.pop()
    elif suma == capacity:
        suma = 0
        racks += 1
        sequence.pop()
    elif suma > capacity:
        suma = 0
        racks += 1

print(racks)
