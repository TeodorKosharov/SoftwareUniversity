def read_next(*args):
    result = [list(str(z) for z in x) for x in args]

    for i in result:
        yield ''.join(i)


for item in read_next("string", (2,), {"d": 1, "I": 2, "c": 3, "t": 4}):
    print(item, end='')
