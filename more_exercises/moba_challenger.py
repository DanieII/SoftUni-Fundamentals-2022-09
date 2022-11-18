all_players = {}
while True:
    command = input()
    if command == "Season end":
        break

    if "->" in command:
        player, position, skill_as_str = command.split(" -> ")
        skill = int(skill_as_str)
        if player not in all_players:
            all_players[player] = {position: skill}
        else:
            if position in all_players[player].keys():
                if all_players[player][position] < skill:
                    all_players[player][position] = skill
            else:
                all_players[player][position] = skill
    # If the input is player vs player
    else:
        player_1, player_2 = command.split(" vs ")
        flag = False
        if player_1 and player_2 in all_players:
            for key, value in all_players[player_1].items():
                for k, v in all_players[player_2].items():
                    # If they have the same position
                    if key == k:
                        # The commented code still works and is slightly better because it checks all
                        # roles and disqualifies the  player if he has no more positions
                        # continue
                        if value > v:
                            flag = True
                            del all_players[player_2]
                            # del all_players[player_2][key]
                            # If the player is out of the season completely
                            # if len(all_players[player_2]) == 0:
                            #     del all_players[player_2]
                            #     break
                        elif v > value:
                            flag = True
                            del all_players[player_1]
                            # del all_players[player_1][key]
                            # if len(all_players[player_1]) == 0:
                            #     del all_players[player_1]
                            #     break
                        else:
                            flag = True
                            break
                if flag:
                    break
# Getting the max scores of each player and sorting them in another dictionary
players_max_score_dict = {}
for user, score in all_players.items():
    max_score = 0
    for current_number in score.values():
        max_score += int(current_number)
    players_max_score_dict[user] = max_score
ordered_players = dict(sorted(players_max_score_dict.items(), key=lambda x: (-x[1], x[0])))

for username, points in ordered_players.items():
    print(f"{username}: {points} skill")
    for k, v in sorted(all_players[username].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {k} <::> {v}")
