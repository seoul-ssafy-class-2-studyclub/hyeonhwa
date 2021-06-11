# 1
def move(d, s):
    dx, dy = idx[d]
    re = []
    for x, y in wind:
        xx = x + dx*s
        yy = y + dy*s
        if xx < 0:
            while xx < 0:
                xx += n
        elif xx >= n:
            while xx >= n:
                xx -= n
        if yy < 0:
            while yy < 0:
                yy += n
        elif yy >= n:
            while yy >= n:
                yy -= n
        re.append((xx, yy))
    return re


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
idx = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
wind = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for _ in range(m):
    d, s = map(int, input().split())
    wind = move(d, s)
    # 2
    for x, y in wind:
        board[x][y] += 1
    
    # 4
    for x, y in wind:
        cnt = 0
        for d in range(2, 9, 2):
            dx, dy = idx[d]
            if 0 <= x+dx < n and 0 <= y+dy < n and board[x+dx][y+dy]:
                cnt += 1
        board[x][y] += cnt
    
    # 5
    new = []
    for x in range(n):
        for y in range(n):
            if board[x][y] >= 2 and (x, y) not in wind:
                new.append((x, y))
                board[x][y] -= 2
    wind = new
res = 0
for i in range(n):
    res += sum(board[i])
print(res)
