cycle_no, X = 0, 1
cycle = {}

def updateCycle(addx_val=0):
    global cycle_no
    global X
    cycle_no += 1

    cycle[cycle_no] = {'sum': X, 'addx_val': addx_val, 'signal_strength': cycle_no*X}
    X += addx_val

with open('data.txt', 'r') as f:
    for line in f:
        if line == '\n': break
        data = line.split()

        if data[0] == 'addx':
            updateCycle()
            updateCycle(int(data[1]))
        elif data[0] == 'noop':
            updateCycle()

sum_of_signal_strength = 0
for i in [20, 60, 100, 140, 180, 220]:
    sum_of_signal_strength += cycle[i]['signal_strength']
    
print(f'The sum of these signal strengths is {sum_of_signal_strength}.')
