ROCK, PAPER, SCISSORS = 1, 2, 3
OUTCOME_WIN, OUTCOME_LOSS, OUTCOME_DRAW = 6, 0, 3
TO_WIN, TO_DRAW = 1, 0

COMPUT_RPS = {'A': ROCK, 'B': PAPER, 'C': SCISSORS}
PLAYER_RPS = {'X': ROCK, 'Y': PAPER, 'Z': SCISSORS}

player_total_score = 0

f = open('data.txt', 'r')
for line in f:
    comp_choice, player_choice = COMPUT_RPS[line[0]], PLAYER_RPS[line[2]]
    round_result = (player_choice - comp_choice) % 3

    if (round_result == TO_DRAW):
        player_total_score += player_choice + OUTCOME_DRAW
    elif (round_result == TO_WIN): 
        player_total_score += player_choice + OUTCOME_WIN
    else: 
        player_total_score += player_choice + OUTCOME_LOSS

f.close()

print(f'Total player score = {player_total_score}.')