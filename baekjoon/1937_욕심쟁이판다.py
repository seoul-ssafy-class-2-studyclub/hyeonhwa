import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def bfs(i, j):
    global res
    # visit = [[0]*n for _ in range(n)]
    # visit[i][j] = 1
    queue = deque()
    queue.append((i, j))
    cnt = 1
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in idx:
                if 0 <= x+dx < n and 0 <= y+dy < n and forest[x+dx][y+dy] > forest[x][y]:
                    queue.append((x+dx, y+dy))
                    # visit[x+dx][y+dy] = 1
        cnt += 1
    res = max(res, cnt-1)


n = int(input())
forest = [[int(i) for i in input().split()] for _ in range(n)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = 0
for i in range(n):
    for j in range(n):
        bfs(i, j)
print(res)