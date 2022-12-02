ROCK, PAPER, SCISSORS = 1, 2, 3
OUTCOME_WIN, OUTCOME_LOSS, OUTCOME_DRAW = 6, 0, 3
TO_WIN, TO_DRAW, TO_LOSE = 1, 0, -1

OUTCOME_SCORE = {TO_WIN: OUTCOME_WIN, TO_LOSE: OUTCOME_LOSS, TO_DRAW: OUTCOME_DRAW}
COMPUT_RPS = {'A': ROCK, 'B': PAPER, 'C': SCISSORS}
PLAYER_RPS = {'X': ROCK, 'Y': PAPER, 'Z': SCISSORS}

player_total_score = 0

f = open('data.txt', 'r')
for line in f:
    comp_choice, player_choice = COMPUT_RPS[line[0]], PLAYER_RPS[line[2]]
    
    round_result = (player_choice - comp_choice + 1) % 3 - 1

    player_total_score += player_choice + OUTCOME_SCORE[round_result]

f.close()

print(f'Total player score = {player_total_score}.')