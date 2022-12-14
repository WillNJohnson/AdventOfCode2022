from collections import deque

def bfs(source, sink_val, graph, nc, nr):
    nodeMap = {}
    nodeMap[source] = {'hasVisited': 0, 'depth': 0}

    # start at vertex source
    q = deque([source])
    
    # while no vertex to visit
    while q:
        # take frontmost node
        node_pos = q.popleft()

        # skip already-visited nodes, and pop the next leftmost node for inspection
        # otherwise, mark this current node as visited
        if nodeMap[node_pos]['hasVisited'] == 1: continue
        nodeMap[node_pos]['hasVisited'] += 1

        # we've reached the sink, so return the search depth
        if graph[node_pos[0]][node_pos[1]] == sink_val: return nodeMap[node_pos]['depth']
        
        # check each adjacent node to current node
        for direction in ['LEFT', 'RIGHT', 'UP', 'DOWN']:
            if (direction == 'LEFT'):       lr, ud = -1, 0
            elif (direction == 'RIGHT'):    lr, ud = 1, 0
            elif (direction == 'UP'):       lr, ud = 0, -1
            else:                           lr, ud = 0, 1

            # get node positions (within bounds of graph)
            cur_x, cur_y = node_pos[0], node_pos[1]
            adj_x, adj_y = cur_x + ud, cur_y + lr
            if adj_x<0 or adj_y<0 or adj_x>nr-1 or adj_y>nc-1: continue

            # if adjacent node has letter in the ordinal position as current node,
            # or is equal to current node minus one letter, then visit this node
            cur_order, adj_order = ord(graph[cur_x][cur_y]), ord(graph[adj_x][adj_y])
            if (cur_order-1 <= adj_order):
                adj_pos = (adj_x, adj_y)

                # update depth by adding weight of cur_pos to the adj_pos (plus one)
                if adj_pos in nodeMap:
                    nodeMap[adj_pos]['depth'] = nodeMap[node_pos]['depth'] + 1
                else: nodeMap[adj_pos] = {'hasVisited': 0, 'depth': nodeMap[node_pos]['depth'] + 1}

                # add adj_position to be checked on the next cycle (i.e. outer loop)
                q.append(adj_pos)

    return -1

hill = []
with open('data.txt', 'r') as f:
    for line in f:
        hill.append(line.strip())

nc = len(hill[0])
nr = len(hill)

# get positions of S and E, represented as node(i, j)
# mark them 'a' and 'z', respectively
for i in range(0, nr):
    for j in range(0, nc):
        if hill[i][j] == 'S':
            S = (i, j)
            hill[i] = hill[i][0:j] + 'a' + hill[i][j+1:nc]
        elif hill[i][j] == 'E':
            E = (i, j)
            hill[i] = hill[i][0:j] + 'z' + hill[i][j+1:nc]

print(f'The fewest number of steps from any elevation "a" to E is {bfs(E, "a", hill, nc, nr)}.')