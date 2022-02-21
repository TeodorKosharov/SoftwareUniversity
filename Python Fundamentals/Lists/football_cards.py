# string = input()
#
# list_of_given_cards = string.split()
# filtered = []
#
# players_a = 11
# players_b = 11
#
# is_game_terminated = False
#
# # Добавяме елементите в новия празен лист и получаваме лист без повтарящи се елементи
# for element in list_of_given_cards:
#
#     if element not in filtered:
#         filtered.append(element)
#
# for element in filtered:
#
#     if 'A' in element:
#         players_a -= 1
#
#         if players_a < 7:
#             is_game_terminated = True
#             break
#
#     elif 'B' in element:
#         players_b -= 1
#
#         if players_b < 7:
#             is_game_terminated = True
#
# if is_game_terminated:
#     print(f'Team A - {players_a}; Team B - {players_b}')
#     print('Game was terminated')
# else:
#     print(f'Team A - {players_a}; Team B - {players_b}')


cards = input().split()
sent_off_players = []

a_players = 11
b_players = 11

for current_card in cards:
    if current_card not in sent_off_players:
        sent_off_players.append(current_card)
        if 'A' in current_card:
            a_players -= 1
        else:
            b_players -= 1

    if a_players < 7 or b_players < 7:
        print(f"Team A - {a_players}; Team B - {b_players}")
        print('Game was terminated')
        exit()

print(f"Team A - {a_players}; Team B - {b_players}")
