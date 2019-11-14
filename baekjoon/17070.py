def go(x=0, y=1, d=1):
    global res
    if x == N-1 and y == N-1:
        res += 1
        return
    if d == 1 and y == N-1:
        return
    if d == 2 and x == N-1:
        return
    for dx, dy in idx[d]:
        n = x+dx
        m = y+dy
        if 0 <= n < N and 0 <= m < N and house[n][m] == 0:
            for nx, ny in notgo[(dx, dy)]:
                if 0 <= n+nx < N and 0 <= m+ny < N and house[n+nx][m+ny] != 0:
                    break
            else:
                if (dx, dy) == (0, 1):
                    d = 1
                if (dx, dy) == (1, 0):
                    d = 2
                if (dx, dy) == (1, 1):
                    d = 3
                go(n, m, d)


N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
idx = {1:[(0, 1), (1, 1)], 2:[(1, 0), (1, 1)], 3:[(1, 0), (0, 1), (1, 1)]}
notgo = {(0, 1): [], (1, 1): [(0, -1), (-1, 0)], (1, 0): []}
res = 0
go()
print(res)
