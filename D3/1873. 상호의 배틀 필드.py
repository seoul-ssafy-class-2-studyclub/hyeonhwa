def start(x, y):
    for string in strings:
        if string == 'S':
            i, j = x, y
            dx, dy = idx[board[x][y]]
            while 0 <= x+dx < H and 0 <= y+dy < W:
                if board[x+dx][y+dy] == '*':
                    board[x+dx][y+dy] = '.'
                    break
                elif board[x+dx][y+dy] == '#':
                    break
                x += dx
                y += dy
            x, y = i, j
        elif string == 'D':
            board[x][y] = 'v'
            dx, dy = idx[board[x][y]]
            if 0 <= x+dx < H and 0 <= y+dy < W and board[x+dx][y+dy] == '.':
                board[x+dx][y+dy] = 'v'
                board[x][y] = '.'
                x += dx
                y += dy
        elif string == 'U':
            board[x][y] = '^'
            dx, dy = idx[board[x][y]]
            if 0 <= x+dx < H and 0 <= y+dy < W and board[x+dx][y+dy] == '.':
                board[x+dx][y+dy] = '^'
                board[x][y] = '.'
                x += dx
                y += dy
        elif string == 'L':
            board[x][y] = '<'
            dx, dy = idx[board[x][y]]
            if 0 <= x+dx < H and 0 <= y+dy < W and board[x+dx][y+dy] == '.':
                board[x+dx][y+dy] = '<'
                board[x][y] = '.'
                x += dx
                y += dy
        else:
            board[x][y] = '>'
            dx, dy = idx[board[x][y]]
            if 0 <= x+dx < H and 0 <= y+dy < W and board[x+dx][y+dy] == '.':
                board[x+dx][y+dy] = '>'
                board[x][y] = '.'
                x += dx
                y += dy


T = int(input())
for t in range(T):
    H, W = map(int, input().split())
    board = [[i for i in input()] for _ in range(H)]
    N = int(input())
    strings = [i for i in input()]
    idx = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    for i in range(H):
        for j in range(W):
            if board[i][j] == '^' or board[i][j] == 'v' or board[i][j] == '>' or board[i][j] == '<':
                x, y = i, j
    start(x, y)
    print('#{}'.format(t+1), end=' ')
    for i in board:
        print(''.join(i))