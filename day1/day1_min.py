best_individual_total_calories, individual_total_calories = 0, 0
with open('data.txt', 'r') as f:
    for line in f:
        try: individual_total_calories += int(line)
        except: best_individual_total_calories = max(individual_total_calories, best_individual_total_calories) ; individual_total_calories = 0
print(f'Elf carrying the most Calories is carry a total of {best_individual_total_calories} Calories.')