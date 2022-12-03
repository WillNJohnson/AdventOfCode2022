ROCK, PAPER, SCISSORS, OUTCOME_WIN, OUTCOME_LOSS, OUTCOME_DRAW, TO_WIN, TO_DRAW, TO_LOSE, player_total_score = 1, 2, 3, 6, 0, 3, 1, 0, -1, 0
OUTCOME_SCORE, RPS = {TO_WIN: OUTCOME_WIN, TO_LOSE: OUTCOME_LOSS, TO_DRAW: OUTCOME_DRAW}, {'A': ROCK, 'B': PAPER, 'C': SCISSORS, 'X': ROCK, 'Y': PAPER, 'Z': SCISSORS}
with open('data.txt', 'r') as f: scores = [RPS[line[2]] + OUTCOME_SCORE[(RPS[line[2]] - RPS[line[0]] + 1) % 3 - 1] for line in f]
print(f'Total player score = {sum(scores)}.')