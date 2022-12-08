def getDirectionScenicValue(M, i, j, nr, nc, direction):
    distance, lr, ud = 0, 0, 0
    cur = M[i][j]

    # get movement (left-right) or (up-down); otherwise no movement remains as 0
    if (direction == 'LEFT'):       lr = -1
    elif (direction == 'RIGHT'):    lr = 1
    elif (direction == 'UP'):       ud = -1
    else:                           ud = 1

    # initial checking position
    ii, jj = i + ud, j + lr

    while ((0 <= ii <= nc) and (0 <= jj <= nr)):
        distance += 1
        if cur <= M[ii][jj]: return distance
        ii, jj = ii + ud, jj + lr
    
    return distance

def main():
    M = []
    scenic_score = 0

    with open('data.txt', 'r') as f:
        for line in f:
            SM = []
            for num in line[0:-1]:
                SM.append(int(num))
            M.append(SM)

    nr, nc = len(M)-1, len(M[0])-1

    # check if inner grid is visible
    for i in range(1, nc):
        for j in range(1, nr):
            temp_scenic_score = 1
            temp_scenic_score*= getDirectionScenicValue(M, i, j, nr, nc, 'LEFT')
            temp_scenic_score*= getDirectionScenicValue(M, i, j, nr, nc, 'RIGHT')
            temp_scenic_score*= getDirectionScenicValue(M, i, j, nr, nc, 'UP')
            temp_scenic_score*= getDirectionScenicValue(M, i, j, nr, nc, 'DOWN')
            
            if temp_scenic_score > scenic_score:
                scenic_score = temp_scenic_score

    print(f'Highest scenic score = {scenic_score}')

if __name__ == "__main__":
    main()