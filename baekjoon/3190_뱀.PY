n = int(input())
k = int(input())
board = [[0]*n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
l = int(input())
direct = [list(input().split()) for _ in range(l)]
idx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
snakes = [(0, 0)]
i, t = 0, 0
direc_idx = 0
dx, dy = idx[0]
while True:
    t += 1
    x, y = snakes[-1]
    if 0 <= x+dx < n and 0 <= y+dy < n:
        if (x+dx, y+dy) in snakes:
            break
        snakes.append((x+dx, y+dy))
        if board[x+dx][y+dy] == 1:
            board[x+dx][y+dy] = 0
        else:
            snakes.pop(0)
    else:
        break
    if i <  len(direct) and direct[i][0] == str(t):
        if direct[i][1] == 'D':
            direc_idx += 1
            if direc_idx == 4:
                direc_idx = 0
            dx, dy = idx[direc_idx]
        else:
            direc_idx -= 1
            if direc_idx == -1:
                direc_idx = 3
            dx, dy = idx[direc_idx]
        i += 1
print(t)
