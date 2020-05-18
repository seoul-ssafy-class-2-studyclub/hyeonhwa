import sys
import collections
input = lambda: sys.stdin.readline().rstrip()

def check():
    visit = [[0]*m for _ in range(n)]
    cnt = 1
    for i in range(1, n-1):
        for j in range(1, m-1):
            if board[i][j] != 0 and visit[i][j] == 0:
                visit[i][j] = cnt
                queue = collections.deque()
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in idx:
                        if 0 <= x+dx < n and 0 <= y+dy < m and board[x+dx][y+dy] != 0 and visit[x+dx][y+dy] == 0:
                            queue.append((x+dx, y+dy))
                            visit[x+dx][y+dy] = cnt
                cnt += 1
            if cnt > 2:
                return True
    return False


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
year = 0
while True:
    melting = [[0]*m for _ in range(n)]
    melt = 0
    for x in range(1, n-1):
        for y in range(1, m-1):
            if board[x][y] != 0:
                melt += 1
                cnt = 0
                for dx, dy in idx:
                    if 0 <= x+dx < n and 0 <= y+dy < m and board[x+dx][y+dy] == 0:
                        cnt += 1
                melting[x][y] = cnt
    if melt == 0:
        year = 0
        break
    for x in range(n):
        for y in range(m):
            if board[x][y] != 0:
                board[x][y] -= melting[x][y]
                if board[x][y] <= 0:
                    board[x][y] = 0
    if check():
        year += 1
        break
    year += 1
print(year)