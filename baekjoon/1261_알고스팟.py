m, n = map(int, input().split())
board = [[i for i in input()] for _ in range(n)]
queue = [(0, 0, 0)]
visit = [[1e10]*m for _ in range(n)]
visit[0][0] = 0
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while queue:
    x, y, cnt = queue.pop(0)
    for dx, dy in idx:
        if 0 <= x+dx < n and 0 <= y+dy < m:
            if board[x+dx][y+dy] == '1':
                if visit[x+dx][y+dy] > cnt+1:
                    visit[x+dx][y+dy] = cnt+1
                    queue.append((x+dx, y+dy, cnt+1))
            else:
                if visit[x+dx][y+dy] > cnt:
                    visit[x+dx][y+dy] = cnt
                    queue.append((x+dx, y+dy, cnt))
print(visit[n-1][m-1])
