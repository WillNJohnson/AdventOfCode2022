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

def touching(rope_head, rope):
    return ((-1 <= (rope_head[0]-rope[0]) <= 1) and (-1 <= (rope_head[1]-rope[1]) <= 1))

def move(position, direction):
    return tuple([sum(x) for x in zip(position, direction)])

def getNextStep(rope_head, rope):
    displ = [rope_head[0] - rope[0], rope_head[1] - rope[1]]
    if (abs(displ[0]) + abs(displ[1])) != 3:
        return tuple([displ[0] >> 1, displ[1] >> 1])

    if not (-1 <= displ[0] <= 1): displ[0] >>= 1
    else: displ[1] >>= 1
    
    return tuple([displ[0], displ[1]])

def runSimulation(rope_length=2):
    # define the steps that head H can take
    step = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

    M_map = {(0, 0): 1}
    rope = [(0, 0)]*(rope_length)

    with open('data.txt', 'r') as f:
        for line in f:
            if line == '\n': break
            data = line.split()

            direction, movement = data[0], int(data[1])

            for _ in range(0, movement):
                rope[0] = move(rope[0], step[direction])

                # for remaining tail trail
                for j in range(1, rope_length):
                    # move tail(i) closer to tail(i-1)
                    if touching(rope[j], rope[j-1]): break
                    nextStep = getNextStep(rope[j-1], rope[j])
                    rope[j] = move(rope[j], nextStep)
                else:
                    # update count of tail(rope_length-1), since that tail node moved
                    try: M_map[rope[rope_length-1]] += 1
                    except: M_map[rope[rope_length-1]] = 1

    print(f'{len(M_map)} positions have been visited by the tail of the rope at least once.')

def main():
    H_length=1
    T_length=9
    if len(sys.argv) > 1:
        try:
            if (T_length := int(sys.argv[1])) < 1: raise Exception()
        except Exception: sys.exit('Tail length must be a positive number.')

    runSimulation(H_length + T_length)

if __name__ == "__main__":
    main()