from collections import deque

import sys
input = lambda: sys.stdin.readline().rstrip()

def go():
    queue = deque()
    queue.append((0, 0, 0))
    visit = [[[0, 0] for _ in range(M)] for __ in range(N)]
    t = 0
    while queue:
        for _ in range(len(queue)):
            x, y, d = queue.popleft()
            if x == N-1 and y == M-1:
                return t+1
            for dx, dy in idx:
                if 0 <= x+dx < N and 0 <= y+dy < M:
                    if d == 0 and board[x+dx][y+dy] == '1' and visit[x+dx][y+dy][1] == 0:
                        queue.append((x+dx, y+dy, 1))
                        visit[x+dx][y+dy][1] = 1
                    elif board[x+dx][y+dy] == '0' and visit[x+dx][y+dy][d] == 0:
                        queue.append((x+dx, y+dy, d))
                        visit[x+dx][y+dy][d] = 1
                    if x+dx == N-1 and y+dy == M-1:
                        return t+2
        t += 1
    return -1

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = go()
print(res)
