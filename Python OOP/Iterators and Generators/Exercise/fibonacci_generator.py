def fibonacci():
    seq = [0, 1]
    first_index = 0
    second_index = 1

    yield seq[first_index]
    yield seq[second_index]

    while True:
        new_number = seq[first_index] + seq[second_index]
        first_index += 1
        second_index += 1
        seq.append(new_number)
        yield new_number


generator = fibonacci()
for i in range(5):
    print(next(generator))
