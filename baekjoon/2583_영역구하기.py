import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(a, b):
    stack = [(a, b)]
    res = 1
    while stack:
        x, y = stack.pop()
        for dx, dy in idx:
            if 0 <= x+dx < n and 0 <= y+dy < m and board[x+dx][y+dy] == 0:
                board[x+dx][y+dy] = -1
                res += 1
                stack.append((x+dx, y+dy))
    return res

n, m, k = map(int, input().split())
board = [[0]*m for _ in range(n)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for i in range(y1, y2):
            board[i][j] = 1
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
area = []
for x in range(n):
    for y in range(m):
        if board[x][y] == 0:
            board[x][y] = -1
            area.append(dfs(x, y))
area.sort()
print(len(area))
print(' '.join(list(map(str, area))))