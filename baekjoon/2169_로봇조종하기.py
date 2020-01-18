def go(x, y, visit=[], total=0):
    global res
    if x == N-1 and y == M-1:
        res = max(res, total)
    for dx, dy in idx:
        if 0 <= x+dx < N and 0 <= y+dy < M and (x+dx, y+dy) not in visit:
            go(x+dx, y+dy, visit+[(x+dx, y+dy)], total+board[x+dx][y+dy])


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
res = 0
idx = [(0, 1), (0, -1), (1, 0)]
go(0, 0)
print(res)
