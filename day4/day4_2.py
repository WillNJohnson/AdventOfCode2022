import re
sum_of_overlapped = 0

def isOverlapped(r0, r1, r2, r3):
     return (r1 >= r2 and r0 <= r3)

with open('data.txt', 'r') as f:
    for line in f:
        r = [int(x) for x in re.split(r',|-', line[0:-1])]
        sum_of_overlapped += isOverlapped(r[0], r[1], r[2], r[3])

print(f'Sum of overlapped assignments = {sum_of_overlapped}.')