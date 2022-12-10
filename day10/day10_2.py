scan = '........................................'
cycle_no, X = 0, 1
draw = '###'
draw_len = len(draw)

crt_row_table = []

def drawPixel(curr_crt_row, sprite_position):
    return (curr_crt_row + sprite_position[len(curr_crt_row)])

def updateCycle(curr_crt_row, sprite_position, addx_val=0, scan=scan):
    global cycle_no
    global X
    cycle_no += 1

    curr_crt_row = drawPixel(curr_crt_row, sprite_position)

    # if % 40, push scanline
    if cycle_no % 40 == 0:
        crt_row_table.append(curr_crt_row)
        curr_crt_row = ''

    X += addx_val

    return curr_crt_row

def updateSpritePosition(X, scan):
    if (X == -1): return ('#' + scan[X-1+draw_len:])[:40]
    
    return (scan[:X-1] + '###' + scan[X-1+draw_len:])[:40]

def main():
    # initial sprite position
    sprite_position = updateSpritePosition(X, scan)
    curr_crt_row = ''

    with open('data.txt', 'r') as f:
        for line in f:
            if line == '\n': break
            data = line.split()

            if data[0] == 'addx':
                curr_crt_row = updateCycle(curr_crt_row=curr_crt_row, sprite_position=sprite_position)
                curr_crt_row = updateCycle(curr_crt_row=curr_crt_row, sprite_position=sprite_position, addx_val=int(data[1]))
                sprite_position = updateSpritePosition(X, scan)
            elif data[0] == 'noop':
                curr_crt_row = updateCycle(curr_crt_row=curr_crt_row, sprite_position=sprite_position)

    print('Puzzle Answer:\n', *crt_row_table, sep='\n')

if __name__ == "__main__":
    main()