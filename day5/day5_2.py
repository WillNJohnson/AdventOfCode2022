import re
sum = 0



with open('data.txt', 'r') as f:
    entries = 0
    stack_map = {}

    # read first line
    # create dictionary key of stack list containing first crate
    for line in f:
        entries = len(line[0:-1]) // 4
        for i in range(0, entries+1):
            k = i * 4 + 1
            stack_map[i] = []
            if line[k] != ' ': 
                stack_map[i].insert(0, line[k])
        break

    # read rest of line until we hit row of numbers
    # populate rest of each stack list with rest of crates
    for line in f:
        if (line[1] == '1'): break

        for i in range(0, entries+1):
            k = i * 4 + 1
            if line[k] != ' ': 
                stack_map[i].insert(0, line[k])

    # skip new line
    for line in f: break

    # rearrange crates by popping and pushing
    for line in f: 
        if (line[1] == '\n'): break

        l = line.split(' ')
        amount, src, des = int(l[1]), int(l[3])-1, int(l[5])-1

        tmp = []
        try:
            for i in range(0, amount):
                tmp.insert(0, stack_map[src].pop(len(stack_map[src])-1))
            for crate in tmp:
                stack_map[des].append(crate)
        except:
            pass

top = ''.join([stack_map[k][-1] for k in stack_map])
print(f'Crate on top of each stack = {top}.')