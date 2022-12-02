best_individual_total_calories, individual_total_calories = 0, 0

f = open('data.txt', 'r')
for line in f:
    try:
        # sum of individual elf's calories to gather total calories
        individual_total_calories += int(line)
    except:
        # non-integer line (space) indicates start of new elf, so check and update calculated calories
        # with the best individual total calories
        if individual_total_calories > best_individual_total_calories:
            best_individual_total_calories = individual_total_calories

        # reset individual calories to calculate next elf's calories
        individual_total_calories = 0

f.close()

print(f'Elf carrying the most Calories is carry a total of {best_individual_total_calories} Calories.')