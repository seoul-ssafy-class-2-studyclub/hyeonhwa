import sys
import collections
input = lambda: sys.stdin.readline().rstrip()

def outer(i, j):
    visit = [[0]*m for _ in range(n)]
    queue = collections.deque(())
    queue.append((i, j))
    visit[i][j] = 1
    while queue:
        x, y = queue.pop()
        for dx, dy in idx:
            if 0 <= x+dx < n and 0 <= y+dy < m and board[x+dx][y+dy] == 0 and visit[x+dx][y+dy] == 0:
                if x+dx == 0 or x+dy == n-1 or y+dy == 0 or y+dy == m-1:
                    return False
                visit[x+dx][y+dy] = 1
                queue.append((x+dx, y+dy))
    return True

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = 0
while True:
    melt = []
    for x in range(n):
        for y in range(m):
            if board[x][y]:
                cnt = 0
                for dx, dy in idx:
                    if 0 <= x+dx < n and 0 <= y+dy < m and board[x+dx][y+dy] == 0:
                        if not outer(x+dx, y+dy):
                            cnt += 1
                if cnt >= 2:
                    melt.append((x, y))    
    for a, b in melt:
        board[a][b] = 0
    if not melt:
        break
    res += 1
print(res)
