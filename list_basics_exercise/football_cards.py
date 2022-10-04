team_a = ["A-" + str(x) for x in range(1, 12)]
team_b = ["B-" + str(x) for x in range(1, 12)]
input_of_given_cards = input().split()
game_over = False
for current_red_card in input_of_given_cards:
    if current_red_card in team_a:
        team_a.remove(current_red_card)
    elif current_red_card in team_b:
        team_b.remove(current_red_card)
    if len(team_a) < 7 or len(team_b) < 7:
        game_over = True
        break
len_of_team_a = len(team_a)
len_of_team_b = len(team_b)
print(f"Team A - {len_of_team_a}; Team B - {len_of_team_b}")
if game_over:
    print("Game was terminated")
