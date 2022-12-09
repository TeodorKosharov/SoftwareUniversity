players_pool = {}

while True:
    command = input()
    if command == "Season end":
        break

    if '->' in command:
        command_list = command.split(' -> ')
        player, position, skill = command_list
        skill = int(skill)

        if player not in players_pool:
            players_pool.update({player: {position: skill}})
        else:
            if position not in players_pool[player]:
                players_pool[player].update({position: skill})
            else:
                if players_pool[player][position] < skill:
                    players_pool[player][position] = skill

    elif 'vs' in command:
        command_list = command.split(' vs ')
        first_player, second_player = command_list

        if first_player in players_pool and second_player in players_pool:
            first_player_positions = players_pool[first_player]
            second_player_positions = players_pool[second_player]

            for first_player_position in first_player_positions:
                flag = False
                for second_player_position in second_player_positions:
                    if first_player_position == second_player_position:
                        first_player_position_score = first_player_positions[first_player_position]
                        second_player_position_score = second_player_positions[second_player_position]
                        if first_player_position_score > second_player_position_score:
                            players_pool.pop(second_player)
                            flag = True
                            break
                        elif first_player_position_score < second_player_position_score:
                            players_pool.pop(first_player)
                            flag = True
                            break
                if flag:
                    break

total_skill = {}
for name in players_pool:
    if name not in total_skill:
        total_skill.update({name: sum(players_pool[name].values())})

total_skill = dict(sorted(total_skill.items(), key=lambda x: (-x[1], x[0])))

for participant, skill in total_skill.items():
    print(f'{participant}: {skill} skill')
    mini_dict = players_pool[participant]
    mini_dict = dict(sorted(mini_dict.items(), key=lambda x: (-x[1], x[0])))
    for curr_position, curr_skill in mini_dict.items():
        print(f'- {curr_position} <::> {curr_skill}')
