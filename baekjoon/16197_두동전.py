n, m = map(int, input().split())
board = [[i for i in input()] for _ in range(n)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
coin = [[0, 0]]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            if coin[0][0]:
                coin[0][1] = (i, j, 0)
                break
            else:
                coin[0][0] = (i, j, 0)
    if coin[0][1]:
        break
res = -1
if coin[0][1]:
    for c1, c2 in coin:
        x1, y1, t1 = c1
        x2, y2, t2 = c2
        flag = 0
        if t1 > 10 or t2 > 10:
            break
        for dx, dy in idx:
            new_coin = [0, 0]
            if 0 <= x1+dx < n and 0 <= y1+dy < m:
                if board[x1+dx][y1+dy] != '#':
                    new_coin[0] = (x1+dx, y1+dy, t1+1)
                elif board[x1+dx][y1+dy] == '#':
                    new_coin[0] = (x1, y1, t1+1)
            if 0 <= x2+dx < n and 0 <= y2+dy < m:
                if board[x2+dx][y2+dy] != '#':
                    new_coin[1] = (x2+dx, y2+dy, t2+1)
                elif board[x2+dx][y2+dy] == '#':
                    new_coin[1] = (x2, y2, t2+1)
            if new_coin[0] and new_coin[1] and (new_coin[0][0] == new_coin[1][0] and new_coin[0][1] == new_coin[1][1]):
                continue
            if new_coin[0] and new_coin[1]:
                coin.append(new_coin)
                continue
            if (new_coin[0] and not new_coin[1]) or (not new_coin[0] and new_coin[1]):
                flag = 1
                if new_coin[0]:
                    res = t2+1
                else:
                    res = t1+1
                break
        if flag:
            break
print(res)
