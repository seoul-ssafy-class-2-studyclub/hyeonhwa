def checkwall(x, y):
    for i in range(x, x+h):
        for j in range(y, y+w):
            if board[i][j] == 1:
                return 1


def move(i, j, k=0):
    res = 0
    queue = [(i, j)]
    while queue:
        nxt = []
        for x, y in queue:
            for dx, dy in idx:
                if 0 <= x+dx < N and 0 <= y+dy < M and 0 <= x+dx+h-1 < N and 0 <= y+dy+w-1 < M:
                    if not checkwall(x+dx, y+dy) and not visit[x+dx][y+dy]:
                        nxt.append((x+dx, y+dy))
                        visit[x+dx][y+dy] = True
        queue = nxt
        res += 1
        if (fr-1, fc-1) in nxt:
            return res
    return -1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
h, w, sr, sc, fr, fc = map(int, input().split())
idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visit[sr-1][sc-1] = True
res = move(sr-1, sc-1)
print(res)
