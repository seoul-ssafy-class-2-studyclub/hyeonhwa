from collections import deque

def go():
    visit = [[[set() for _ in range(5)] for __ in range(M)] for ___ in range(N)]
    queue = deque()
    queue.append(start)
    t = 0
    while queue:
        for _ in range(len(queue)):
            x, y, d = queue.popleft()
            for i in range(1, 5):
                if d == i:
                    continue
                dx, dy = idx[i]
                if 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] != '#' and (not visit[x+dx][y+dy][i] or (visit[x+dx][y+dy][i] and len(visit[x+dx][y+dy][i]) <= len(visit[x][y][d]))):
                    if board[x+dx][y+dy] == 'C':
                        visit[x+dx][y+dy][i].add((x+dx, y+dy))
                        visit[x+dx][y+dy][i] = visit[x+dx][y+dy][i].union(visit[x][y][d])
                    elif board[x+dx][y+dy] == '.' or board[x+dx][y+dy] == 'S':
                        visit[x+dx][y+dy][i] = visit[x][y][d]
                    if (x+dx, y+dy, i) not in queue:
                        queue.append((x+dx, y+dy, i))
                    if len(visit[x+dx][y+dy][i]) == pre:
                        return t+1
        t += 1
    return -1


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
start = ''
pre = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'S':
            start = (i, j, 0)
        elif board[i][j] == 'C':
            pre += 1
idx = {1:(-1, 0), 2:(1, 0), 3:(0, -1), 4:(0, 1)}
print(go())
