import sys

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

To determine diagonal movement for each tail node:
    Take sum of absolute values for displacement on x axis and displacement on y axis
    If sum is three, then half the value where a displacement value is equal to two
    
'''

def touching(H_pos, T_pos):
    return ((-1 <= (H_pos[0]-T_pos[0]) <= 1) and (-1 <= (H_pos[1]-T_pos[1]) <= 1))

def move(position, direction):
    return tuple([sum(x) for x in zip(position, direction)])

def getNextStep(H_pos, T_pos):
    displ = [H_pos[0] - T_pos[0], H_pos[1] - T_pos[1]]
    if (abs(displ[0]) + abs(displ[1])) != 3:
        return tuple([displ[0] >> 1, displ[1] >> 1])

    if not (-1 <= displ[0] <= 1): displ[0] >>= 1
    else: displ[1] >>= 1
    
    return tuple([displ[0], displ[1]])

def runSimulation(T_length=1):
    # define the steps that head H can take
    step = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

    M_map = {(0, 0): 1}
    H_pos, T_pos = (0, 0), [(0, 0)]*T_length
    
    with open('data.txt', 'r') as f:
        for line in f:
            if line == '\n': break
            data = line.split()

            direction, movement = data[0], int(data[1])

            for _ in range(0, movement):
                H_pos = move(H_pos, step[direction])

                # move tail(0) closer to head
                if touching(H_pos, T_pos[0]): continue
                nextStep = getNextStep(H_pos, T_pos[0])
                T_pos[0] = move(T_pos[0], nextStep)

                if T_length == 1: 
                    try: M_map[T_pos[0]] += 1
                    except: M_map[T_pos[0]] = 1
                    continue

                # for remaining tail trail
                for j in range(1, T_length):
                    # move tail(i) closer to tail(i-1)
                    if touching(T_pos[j], T_pos[j-1]): j = T_length ; continue
                    nextStep = getNextStep(T_pos[j-1], T_pos[j])
                    T_pos[j] = move(T_pos[j], nextStep)
                    
                    # update tail(length-1) if it moved
                    if (j == T_length-1):
                        try: M_map[T_pos[T_length-1]] += 1
                        except: M_map[T_pos[T_length-1]] = 1

    print(f'{len(M_map)} positions have been visited by the tail of the rope at least once.')

def main():
    T_length=9
    if len(sys.argv) > 1:
        try:
            if (T_length := int(sys.argv[1])) < 1: raise Exception()
        except Exception: sys.exit('Enter a positive number.')

    runSimulation(T_length)

if __name__ == "__main__":
    main()