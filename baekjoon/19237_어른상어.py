idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m, k = map(int, input().split())
board, shark = [], [[] for _ in range(m)]
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j]:
            shark[board[i][j]-1].extend([i, j])
            board[i][j] = [board[i][j], k]
d = list(map(int, input().split()))
for i in range(m):
    shark[i].append(d[i])
direction = [[] for _ in range(m)]
for i in range(m):
    for _ in range(4):
        direction[i].append(list(map(int, input().split())))
res = 0
while True:
    res += 1
    if res == 1001:
        print(-1)
        break
    # 상어 중복 여부 확인
    check = [[0]*n for _ in range(n)]
    for i in range(m):
        if shark[i]:
            x, y, loc, flag = shark[i][0], shark[i][1], shark[i][2], 0
            for j in range(4):
                ndir = direction[i][loc-1][j]
                dx, dy = idx[ndir-1]
                if 0 <= x+dx < n and 0 <= y+dy < n:
                    if board[x+dx][y+dy] == 0:
                        flag = 1
                        break
            if not flag:
                for j in range(4):
                    ndir = direction[i][loc-1][j]
                    dx, dy = idx[ndir-1]
                    if 0 <= x+dx < n and 0 <= y+dy < n:
                        if board[x+dx][y+dy][0] == i+1:
                            break
            if check[x+dx][y+dy]:
                if check[x+dx][y+dy] < i+1:
                    shark[i] = 0
                else:
                    shark[check[x+dx][y+dy]-1] = 0
            else:
                check[x+dx][y+dy] = i+1
                shark[i] = [x+dx, y+dy, ndir]
    
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                board[i][j][1] -= 1
                if board[i][j][1] == 0:
                    board[i][j] = 0
    
    for i in range(m):
        if shark[i]:
            x, y, direc = shark[i]
            board[x][y] = [i+1, k]
        
    if shark.count(0) == m-1:
        print(res)
        break
