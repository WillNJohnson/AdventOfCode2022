best_individual_total_calories, individual_total_calories = 0, 0

all_calories = []

f = open('data.txt', 'r')
for line in f:
    try:
        # sum of individual elf's calories to gather total calories
        individual_total_calories += int(line)
    except:
        # append individual total calories to list
        all_calories.append(individual_total_calories)

        # reset individual calories to calculate next elf's calories
        individual_total_calories = 0

f.close()

all_calories.sort(reverse=True)
sum_of_top_three_calories = sum(all_calories[0:3])

print(f'Total Calories of top three elves is {sum_of_top_three_calories} Calories.')