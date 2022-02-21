def indices_checker(first_ind: int, second_ind: int, passed_sequence: list):
    conditions = [
        0 <= first_ind <= len(passed_sequence) - 1,
        0 <= second_ind <= len(passed_sequence) - 1,
        first_ind != second_ind
    ]

    if all(conditions):
        return True
    return False


sequence = [x for x in input().split()]
moves = 0

while True:

    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
        exit()

    given_str = input()
    if given_str == 'end':
        print("Sorry you lose :(")
        print(*sequence)
        exit()

    first_index = int(given_str.split()[0])
    second_index = int(given_str.split()[1])
    moves += 1

    if indices_checker(first_index, second_index, sequence):
        if sequence[first_index] == sequence[second_index]:
            print(f"Congrats! You have found matching elements - {sequence[first_index]}!")
            sequence = [x for x in sequence if x != sequence[first_index]]
        else:
            print("Try again!")
    else:
        middle_index = len(sequence) // 2
        sequence.insert(middle_index, f'-{moves}a')
        sequence.insert(middle_index, f'-{moves}a')
        print("Invalid input! Adding additional elements to the board")
