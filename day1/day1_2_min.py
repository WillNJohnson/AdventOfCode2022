best_individual_total_calories, individual_total_calories, all_calories = 0, 0, []
with open('data.txt', 'r') as f:
    for line in f:
        try: individual_total_calories += int(line)
        except: all_calories.append(individual_total_calories) ; individual_total_calories = 0
print(f'Total Calories of top three elves is {sum(sorted(all_calories, reverse=True)[:3])} Calories.')