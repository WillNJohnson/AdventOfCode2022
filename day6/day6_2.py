n_distinct = 14
with open('data.txt', 'r') as f:
    line = f.read()
    for i in range(0, len(line)-n_distinct-1):
        if len(set(*line[i:i+n_distinct].split())) == n_distinct:
            print(f'Characters need to be processed: {i+n_distinct}')
            break