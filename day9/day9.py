'''
Assumptions:
- Matrix is unbounded, so should not create a matrix.
- Position can be negative.

We'll track position as node (x, y)
- x can go left (-1) or right (1)
- y can go up (1) or down (-1)

Keep a map, and update number of visits. Starting point is at 
node (0, 0) and we will initialize position count as 1.

Visualization:

   :
   30 31 32 33
   20 21 22 23
   10 11 12 13
.. 00 01 02 03 ..
   :

'''

def touching(H_pos, T_pos):
    return ((-1 <= (H_pos[0]-T_pos[0]) <= 1) and (-1 <= (H_pos[1]-T_pos[1]) <= 1))

def move(position, direction):
    return tuple([sum(x) for x in zip(position, direction)])

# define the step (as well as diagonal step)
step = {
    'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)
}

M_map = {(0, 0): 1}
H_pos, T_pos = (0, 0), (0, 0)

with open('data.txt', 'r') as f:
    for line in f:
        if line == '\n': break
        data = line.split()

        direction, movement = data[0], int(data[1])

        for i in range(0, movement):
            H_prev_pos = H_pos
            H_pos = move(H_pos, step[direction])

            if touching(H_pos, T_pos): continue

            # update T_pos
            T_pos = H_prev_pos
            try: M_map[T_pos] += 1
            except: M_map[T_pos] = 1

print(f'{len(M_map)} positions have been visited at least once.')
