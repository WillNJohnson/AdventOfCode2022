import re
sum_of_contained = 0

def isContained(r0, r1, r2, r3):
     return (r0 <= r2 and r1 >= r3) or (r0 >= r2 and r1 <= r3)

with open('data.txt', 'r') as f:
    for line in f:
        r = [int(x) for x in re.split(r',|-', line[0:-1])]
        sum_of_contained += isContained(r[0], r[1], r[2], r[3])

print(f'Sum of contained assignments = {sum_of_contained}.')