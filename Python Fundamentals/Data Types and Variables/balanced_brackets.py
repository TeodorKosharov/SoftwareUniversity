n = int(input())

first_condition = False
second_condition = False

first_bracket_counter = 0
second_bracket_counter = 0

is_first_bracket_available = False

for line in range(1, n + 1):

    symbol = input()

    if symbol == '(':
        first_condition = True
        is_first_bracket_available = True    # Променлива за проверка дали започваме с отваряща скоба
        first_bracket_counter += 1

        if first_bracket_counter > 1:        # Ако отварящите скоби станат повече от една, то нарушаваме условието - да не използваме вложени скоби
            first_condition = False

    if is_first_bracket_available:
        if symbol == ')':
            second_condition = True
            second_bracket_counter += 1

            if second_bracket_counter > 1:  # Отново спазваме правилото без вложени скоби
                second_condition = False

    if first_condition and second_condition:   # Главното условие е изпълнено => зануляваме броячите и започваме да правим проверки дали е изпълнено отново главното условие
        first_bracket_counter = 0
        second_bracket_counter = 0

if first_condition and second_condition:
    print('BALANCED')
else:
    print('UNBALANCED')
