import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def bfs(now):
    queue = deque()
    queue.append(now)
    while queue:
        x, y, z = queue.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < n and 0 <= y+dy < m and not visit[x+dx][y+dy][z] and board[x+dx][y+dy] != '#':
                if board[x+dx][y+dy] == '1':
                    return visit[x][y][z] + 1
                elif 'a' <= board[x+dx][y+dy] <= 'f':
                    nxt = z | (1 << (ord(board[x+dx][y+dy]) - ord('a')))
                    if not visit[x+dx][y+dy][nxt]:
                        visit[x+dx][y+dy][nxt] = visit[x][y][z] + 1
                        queue.append((x+dx, y+dy, nxt))
                elif 'A' <= board[x+dx][y+dy] <= 'F':
                    nxt = z & (1 << (ord(board[x+dx][y+dy])-ord('A')))
                    if nxt:
                        visit[x+dx][y+dy][z] = visit[x][y][z] + 1
                        queue.append((x+dx, y+dy, z))
                else:
                    visit[x+dx][y+dy][z] = visit[x][y][z] + 1
                    queue.append((x+dx, y+dy, z))
    return -1


n, m = map(int, input().split())
board = [[i for i in input()] for _ in range(n)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visit = [[[0]*64 for __ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == '0':
            now = (i, j, 0)
res = bfs(now)
print(res)