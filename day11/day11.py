monkey = {}

def prod(l):
    x = 1
    return [(x:=x*y) for y in l][-1]

def doNProcessThrows(N, monkey):
    for _ in range(N):
        processThrow(monkey)
    return monkey

def processThrow(monkey):
    new = 0
    for n in range(len(monkey)):
        starting_items = monkey[n]['starting']
        while starting_items != []:
            old = monkey[n]['starting'][0]
            new = eval(monkey[n]['op']) // 3
            if new % monkey[n]['divisible'] == 0:
                monkey[monkey[n]['on_true']]['starting'].append(new)
            else:
                monkey[monkey[n]['on_false']]['starting'].append(new)
            starting_items.pop(0)
            monkey[n]['inspections'] += 1

    return monkey

with open('data.txt', 'r') as f:
    starting_items = []
    operation = ''
    test_divisibility_by = 0
    on_true_throw_to = 0
    on_false_throw_to = 0

    # parse data into a dictionary
    n = 0
    for line in f:
        data = line.split()

        if data == []:
            monkey[n] = {'starting': starting_items, 'op': operation, 'divisible': test_divisibility_by, 'on_true': on_true_throw_to, 'on_false': on_false_throw_to, 'inspections': 0}
            n += 1
        elif data[0] == 'Starting':
            starting_items = [int(d.strip(',')) for d in data[2:]]
        elif data[0] == 'Operation:':
            operation = ' '.join(data[1:]).split('=')[-1]
        elif data[0] == 'Test:':
            test_divisibility_by = int(data[-1])
        elif ' '.join(data[0:2]) == 'If true:':
            on_true_throw_to = int(data[-1])
        elif ' '.join(data[0:2]) == 'If false:':
            on_false_throw_to = int(data[-1])

    monkey[n] = {'starting': starting_items, 'op': operation, 'divisible': test_divisibility_by, 'on_true': on_true_throw_to, 'on_false': on_false_throw_to, 'inspections': 0}

# do calculation of monkey throws
monkey = doNProcessThrows(20, monkey)

# get top 2 number of inspections
top_two_inspections = sorted([monkey[n]['inspections'] for n in monkey])[-2:]

print(f'The level of monkey business is {prod(top_two_inspections)}.')
