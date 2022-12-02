ROCK, PAPER, SCISSORS = 1, 2, 3
OUTCOME_WIN, OUTCOME_LOSS, OUTCOME_DRAW = 6, 0, 3
TO_WIN, TO_DRAW, TO_LOSE = 1, 0, -1

COMPUT_RPS = {'A': ROCK, 'B': PAPER, 'C': SCISSORS}
OUTCOME_RPS = {'X': TO_LOSE, 'Y': TO_DRAW, 'Z': TO_WIN}

player_total_score = 0

f = open('data.txt', 'r')
for line in f:
    comp_choice, player_outcome_choice = COMPUT_RPS[line[0]], OUTCOME_RPS[line[2]]

    if (player_outcome_choice == TO_DRAW):
        player_choice = (comp_choice-1) % 3 + 1
        player_total_score += player_choice + OUTCOME_DRAW
    elif (player_outcome_choice == TO_LOSE):
        player_choice = (comp_choice-2) % 3 + 1
        player_total_score += player_choice + OUTCOME_LOSS
    else:
        player_choice = (comp_choice) % 3 + 1
        player_total_score += player_choice + OUTCOME_WIN

f.close()

print(f'Total player score = {player_total_score}.')