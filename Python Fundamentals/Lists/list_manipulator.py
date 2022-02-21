def get_rightmost_value(given_list: list, look_value: int):
    for index in range(len(given_list)):
        if look_value == given_list[index]:
            needed_index = index
    return needed_index


initial_list = list(map(int, input().split(' ')))

while True:
    command = input()
    if command == 'end':
        print(initial_list)
        break
    command_list = command.split()
    action = command_list[0]

    if action == 'exchange':
        index = int(command_list[1])
        if index < 0 or index > len(initial_list) - 1:
            print("Invalid index")
        else:
            initial_list = initial_list[index + 1:] + initial_list[:index + 1]

    elif action == 'max':
        if command_list[1] == 'even':
            evens = [x for x in initial_list if x % 2 == 0]
            if evens:
                max_even = max(evens)
                print(get_rightmost_value(initial_list, max_even))
            else:
                print("No matches")

        elif command_list[1] == 'odd':
            odds = [x for x in initial_list if x % 2 == 1]
            if odds:
                max_odd = max(odds)
                print(get_rightmost_value(initial_list, max_odd))
            else:
                print("No matches")

    elif action == 'min':
        if command_list[1] == 'even':
            evens = [x for x in initial_list if x % 2 == 0]
            if evens:
                min_even = min(evens)
                print(get_rightmost_value(initial_list, min_even))
            else:
                print("No matches")

        elif command_list[1] == 'odd':
            odds = [x for x in initial_list if x % 2 == 1]
            if odds:
                min_odd = min(odds)
                print(get_rightmost_value(initial_list, min_odd))
            else:
                print("No matches")

    elif action == 'first':
        count = int(command_list[1])
        if count <= len(initial_list):
            if command_list[2] == 'even':
                first_evens = []
                for index in range(len(initial_list)):
                    if initial_list[index] % 2 == 0:
                        first_evens.append(initial_list[index])
                        count -= 1
                        if count == 0:
                            break
                if first_evens:
                    print(first_evens)
                else:
                    print('[]')

            elif command_list[2] == 'odd':
                first_odds = []
                for index in range(len(initial_list)):
                    if initial_list[index] % 2 == 1:
                        first_odds.append(initial_list[index])
                        count -= 1
                        if count == 0:
                            break
                if first_odds:
                    print(first_odds)
                else:
                    print('[]')
        else:
            print("Invalid count")

    elif action == 'last':
        count = int(command_list[1])
        if count <= len(initial_list):
            if command_list[2] == 'even':
                last_evens = []
                for index in range(-1, -(len(initial_list)) - 1, -1):
                    if initial_list[index] % 2 == 0:
                        last_evens.append(initial_list[index])
                        count -= 1
                        if count == 0:
                            break
                if last_evens:
                    last_evens.reverse()
                    print(last_evens)
                else:
                    print('[]')
            elif command_list[2] == 'odd':
                last_odds = []
                for index in range(-1, -(len(initial_list)) - 1, -1):
                    if initial_list[index] % 2 == 1:
                        last_odds.append(initial_list[index])
                        count -= 1
                        if count == 0:
                            break
                if last_odds:
                    last_odds.reverse()
                    print(last_odds)
                else:
                    print('[]')
        else:
            print("Invalid count")
