n = int(input())

pianist_data = {}

for _ in range(n):
    inp = input().split('|')
    piece, composer, key = inp
    pianist_data[piece] = [composer, key]

while True:
    inp = input().split('|')
    if inp[0] == 'Stop':
        break
    command = inp[0]

    if command == 'Add':
        piece = inp[1]
        if piece in pianist_data:
            print(f"{piece} is already in the collection!")
        elif piece not in pianist_data:
            composer = inp[2]
            key = inp[3]
            pianist_data[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == 'Remove':
        piece = inp[1]
        if piece in pianist_data:
            print(f"Successfully removed {piece}!")
            pianist_data.pop(piece)
        elif piece not in pianist_data:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == 'ChangeKey':
        piece = inp[1]
        new_key = inp[2]

        if piece in pianist_data:
            print(f"Changed the key of {piece} to {new_key}!")
            pianist_data[piece][1] = new_key
        elif piece not in pianist_data:
            print(f"Invalid operation! {piece} does not exist in the collection.")

pianist_data = dict(sorted(pianist_data.items(), key=lambda x: (x[0], x[1][0])))

for k, v in pianist_data.items():
    print(f"{k} -> Composer: {v[0]}, Key: {v[1]}")
