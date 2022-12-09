matrix = []

for row in range(int(input())):
    matrix.append([input()])

search_symbol = input()

search_symbol_indices = None

for row_index in range(len(matrix)):
    element = matrix[row_index][0]
    for symbol_index in range(len(element)):
        if element[symbol_index] == search_symbol:
            search_symbol_indices = (row_index, symbol_index)
            print(search_symbol_indices)
            exit(0)
print(f"{search_symbol} does not occur in the matrix")
