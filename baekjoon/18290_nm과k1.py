def choose(arr):
    global res
    if len(arr) == k:
        value = 0
        for x, y in arr:
            value += board[x][y]
        res = max(res, value)
        return
    for i in range(n):
        for j in range(n):
            if not sol(i, j, arr) or visit[i][j]:
                continue
            visit[i][j] = 1
            choose(arr+[(i, j)])
            visit[i][j] = 0


def sol(x, y, check):
    idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for xx, yy in check:
        for dx, dy in idx:
            if 0 <= xx+dx < n and 0 <= yy+dy < m:
                if xx + dx == x and yy+dy == y:
                    return False
    return True


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
res = -1e10
choose([])
print(res)
