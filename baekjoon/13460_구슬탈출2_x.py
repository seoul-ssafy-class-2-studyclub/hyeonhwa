def go(x1, y1, x2, y2, cnt):
    global res
    if cnt >= 10:
        return
    i, j = x1, y1
    n, m = x2, y2
    for dx, dy in idx:
        x1, y1 = i, j
        x2, y2 = n, m
        while 0 <= x1+dx < N and 0 <= y1+dy < M:
            if board[x1+dx][y1+dy] == '.':
                x1 += dx
                y1 += dy
            elif board[x1+dx][y1+dy] != '.':
                if board[x1+dx][y1+dy] == 'O':
                    res = min(res, cnt)
                    return
                break
        while 0 <= x2+dx < N and 0 <= y2+dy < M:
            if board[x2+dx][y2+dy] == '.':
                x2 += dx
                y2 += dy
            elif board[x2+dx][y2+dy] != '.':
                if board[x2+dx][y2+dy] == 'O':
                    return
                break
        while 0 <= x1+dx < N and 0 <= y1+dy < M:
            if board[x1+dx][y1+dy] == '.':
                x1 += dx
                y1 += dy
            elif board[x1+dx][y1+dy] != '.':
                if board[x1+dx][y1+dy] == 'O':
                    res = min(res, cnt)
                    return
                break
        go(x1, y1, x2, y2, cnt+1)


N, M = map(int, input().split())
board = [[i for i in input()] for _ in range(N)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for x in range(N):
    for y in range(M):
        if board[x][y] == 'R':
            red = (x, y)
        elif board[x][y] == 'B':
            blue = (x, y)
res = 987654321
go(red[0], red[1], blue[0], blue[1], 0)
print(res)
