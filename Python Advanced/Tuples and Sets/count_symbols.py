text = input()

symbols = {}

for char in text:
    if char not in symbols:
        symbols[char] = 0
    symbols[char] += 1

symbols = dict(sorted(symbols.items(), key=lambda x: x[0]))

for data_tuple in symbols.items():
    print(f'{data_tuple[0]}: {data_tuple[1]} time/s')
