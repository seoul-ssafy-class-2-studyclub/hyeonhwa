def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    cnt = 0
    for dx, dy in idx:
        if 0 <= x+dx < n and 0 <= y+dy < m and board[x+dx][y+dy] < board[x][y]:
            if visit[x+dx][y+dy] >= 0:
                cnt += visit[x+dx][y+dy]
            else:
                cnt += dfs(x+dx, y+dy)
    visit[x][y] = cnt
    return cnt


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
stack = [(0, 0)]
idx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
visit = [[-1]*m for _ in range(n)]
visit[0][0] = 0
print(dfs(0, 0))
