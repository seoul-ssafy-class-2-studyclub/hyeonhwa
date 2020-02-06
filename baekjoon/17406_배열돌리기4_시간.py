from pprint import pprint

def rotate(sx, sy, ex, ey):
    if sx == ex and sy == ey:
        return
    x, y = sx, sy
    dx, dy = 0, 1
    arr = [0] * ((ex-sx + ey-sy+2)*2-4)
    arr[0] = board[x+1][y]
    k = 1
    while sx <= x+dx <= ex and sy <= y+dy <= ey and k < len(arr):
        arr[k] = board[x][y]
        x += dx
        y += dy
        if (x, y) == (ex, sy) or (x, y) == (ex, ey) or (x, y) == (sx, ey):
            dx, dy = idx[(dx, dy)]
        k += 1
    k = 0
    x, y = sx, sy
    dx, dy = 0, 1
    while sx <= x+dx <= ex and sy <= y+dy <= ey and k < len(arr):
        board[x][y] = arr[k]
        x += dx
        y += dy
        if (x, y) == (ex, sy) or (x, y) == (ex, ey) or (x, y) == (sx, ey):
            dx, dy = idx[(dx, dy)]
        k += 1
    rotate(sx+1, sy+1, ex-1, ey-1)


def cals(arr):
    res = 1e9
    for i in arr:
        if sum(i) < res:
            res = sum(i)
    return res


def dfs(k, arr):
    if k == K:
        if arr not in order:
            order.append(arr)
        return
    for i in range(K):
        if visited[i] is False:
            visited[i] = True
            dfs(k+1, arr+[i])
            visited[i] = False


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
idx = {(-1, 0):(0, 1), (1, 0):(0, -1), (0, -1):(-1, 0), (0, 1):(1, 0)}
rd = [list(map(int, input().split())) for _ in range(K)]
order = []
res = 1e9
visited = [False]*K
dfs(0, [])
for l in order:
    reboard = [i[:] for i in board]
    for i in l:
        s, r, c = rd[i]
        rotate(s-c-1, r-c-1, s+c-1, r+c-1)
    if cals(board) < res:
        res = cals(board)
    board = reboard
print(res)