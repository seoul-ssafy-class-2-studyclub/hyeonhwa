n, m = map(int, input().split())
board = [[i for i in input()] for _ in range(n)]
res = 0
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            queue = [(i, j, 0)]
            visit = [[0]*m for _ in range(n)]
            visit[i][j] = 1
            while queue:
                x, y, t = queue.pop(0)
                for dx, dy in idx:
                    if 0 <= x+dx < n and 0 <= y+dy < m and board[x+dx][y+dy] == 'L' and not visit[x+dx][y+dy]:
                        queue.append((x+dx, y+dy, t+1))
                        visit[x+dx][y+dy] = 1
            res = max(t, res)
print(res)
