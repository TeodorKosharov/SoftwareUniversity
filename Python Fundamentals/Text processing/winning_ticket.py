def get_winning_symbol(ticket):
    for char in win_symbols:
        if char in ticket:
            return char
    return None


def repeating_winning_symbol(half):
    repeated = 0
    uninterupted = 0

    for chr in half:
        if chr == winning_symbol:
            repeated += 1
            if repeated >= 6:
                uninterupted = repeated
        else:
            repeated = 0
    return uninterupted


tickets = input().split(', ')
win_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    ticket = ticket.strip()

    if len(ticket) == 20:
        left_half = ticket[:10]
        right_half = ticket[10:]
        winning_symbol = get_winning_symbol(left_half)
        repeated_left = repeating_winning_symbol(left_half)
        repeated_right = repeating_winning_symbol(right_half)

        if repeated_left < 6 or repeated_right < 6:
            print(f'ticket "{ticket}" - no match')
        elif repeated_right == 10 and repeated_left == 10:
            print(f'ticket "{ticket}" - {10}{winning_symbol} Jackpot!')
        else:
            if repeated_left >= 6 and repeated_right >= 6:
                print(f'ticket "{ticket}" - {min(repeated_left, repeated_right)}{winning_symbol}')
            else:
                print(f'ticket "{ticket}" - no match')
    else:
        print('invalid ticket')

