from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

def arrive(x, y):
    queue = deque()
    queue.append((x, y, 0, 0))
    visit = [[[0]*W for _ in range(H)] for _ in range(K+1)]
    for i in range(K+1):
        visit[i][0][0] = 1
    res = 1e9
    while queue:
        x, y, h, cnt = queue.popleft()
        if h < K:
            for dx, dy in horse:
                if 0 <= x+dx < H and 0 <= y+dy < W and board[x+dx][y+dy] == 0 and visit[h+1][x+dx][y+dy] == 0:
                    if x+dx == H-1 and y+dy == W-1:
                        res = min(res, cnt+1)
                    visit[h+1][x+dx][y+dy] = 1
                    queue.append((x+dx, y+dy, h+1, cnt+1))
            for dx, dy in idx:
                if 0 <= x+dx < H and 0 <= y+dy < W and board[x+dx][y+dy] == 0 and visit[h][x+dx][y+dy] == 0:
                    if x+dx == H-1 and y+dy == W-1:
                        res = min(res, cnt+1)
                    visit[h][x+dx][y+dy] = 1
                    queue.append((x+dx, y+dy, h, cnt+1))
        else:
            for dx, dy in idx:
                if 0 <= x+dx < H and 0 <= y+dy < W and board[x+dx][y+dy] == 0 and visit[h][x+dx][y+dy] == 0:
                    if x+dx == H-1 and y+dy == W-1:
                        res = min(res, cnt+1)
                    visit[h][x+dx][y+dy] = 1
                    queue.append((x+dx, y+dy, h, cnt+1))
    if res == 1e9:
        res = -1
    return res

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
if W == 1 and H == 1 and board[0][0] == 0:
    print(0)
elif board[0][0] == 1:
    print(-1)
else:
    horse = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
    idx = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    res = arrive(0, 0)
    print(res)
