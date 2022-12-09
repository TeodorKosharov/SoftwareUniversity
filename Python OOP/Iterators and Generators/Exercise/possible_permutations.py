from itertools import permutations


def possible_permutations(some_list):
    for i in permutations(some_list):
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]
