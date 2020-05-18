import sys
import collections
input = lambda: sys.stdin.readline().rstrip()

def check(i, j):
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
time = 0
res = 0
while True:
    melting = [[0]*m for _ in range(n)]
    flag = 0
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                flag += 1
                for dx, dy in idx:
                    if 0 <= i+dx < n and 0 <= j+dy < m and board[i+dx][j+dy] == 0:
                        if not check(i, j):
                            melting[i][j] = 1
                            break
    if flag == 0:
        break
    else:
        res = flag
    for i in range(1, n):
        for j in range(1, m):
            if melting[i][j] == 1:
                board[i][j] = 0
    time += 1
print(str(time) + '\n' + str(res))