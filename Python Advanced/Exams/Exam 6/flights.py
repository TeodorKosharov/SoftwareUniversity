def flights(*args):
    destinations = {}
    last_destionation = ''

    for element in args:

        if element == 'Finish':
            break

        if type(element) == str:
            last_destionation = element

        if last_destionation not in destinations:
            destinations[element] = 0
            continue

        if type(element) == int:
            destinations[last_destionation] += int(element)

    if 'Finish' in destinations:
        destinations.pop('Finish')

    return destinations


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
