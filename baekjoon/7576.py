from collections import deque

def no():
    for i in range(N):
        if 0 in board[i]:
            return True
    return False


def tomatoes():
    cnt = 0
    queue = tomato
    nxt = deque()
    while queue:
        x, y = queue.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] == 0:
                board[x+dx][y+dy] = 1
                nxt.append((x+dx, y+dy))
        if not queue:
            cnt += 1
            queue = nxt
            nxt = deque()
    if no():
        cnt = 0
    return cnt

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
tomato = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            tomato.append((i, j))
if not no():
    res = 0
else:
    res = tomatoes()-1
print(res)