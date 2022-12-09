def get_ampersand_indices(text: str):
    start_end = []
    for index in range(len(text)):
        if text[index] == '&':
            start_end.append(index)
    return start_end


def get_arrow_indices(text: str):
    start_end = []
    for index in range(len(text)):
        if text[index] == '<' or text[index] == '>':
            start_end.append(index)
    return start_end


keys = [int(x) for x in input().split()]

keys_length = len(keys) - 1

while True:
    inp = input()
    if inp == 'find':
        exit()

    hidden_message = ''
    key_index = 0

    for char in inp:
        char = chr(ord(char) - keys[key_index])
        key_index += 1
        if key_index > keys_length:
            key_index = 0

        hidden_message += char

    treasure_start = get_ampersand_indices(hidden_message)[0]
    treasure_end = get_ampersand_indices(hidden_message)[1]
    treasure = hidden_message[treasure_start + 1: treasure_end]

    coordinates_start = get_arrow_indices(hidden_message)[0]
    coordinates_end = get_arrow_indices(hidden_message)[1]
    coordinates = hidden_message[coordinates_start + 1: coordinates_end]
    print(f'Found {treasure} at {coordinates}')
