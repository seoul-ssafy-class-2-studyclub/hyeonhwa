def go(x, y, d):
    if d == '1':
        if 0 <= y+1 < M:
            y += 1
            dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]
            if board[x][y] == '0':
                board[x][y] = dice[2]
            else:
                dice[2] = board[x][y]
                board[x][y] = '0'
    elif d == '2':
        if 0 <= y-1 < M:
            y -= 1
            dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]
            if board[x][y] == '0':
                board[x][y] = dice[2]
            else:
                dice[2] = board[x][y]
                board[x][y] = '0'
    elif d == '3':
        if 0 <= x-1 < N:
            x -= 1
            dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
            if board[x][y] == '0':
                board[x][y] = dice[2]
            else:
                dice[2] = board[x][y]
                board[x][y] = '0'
    else:
        if 0 < x+1 < N:
            x += 1
            dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
            if board[x][y] == '0':
                board[x][y] = dice[2]
            else:
                dice[2] = board[x][y]
                board[x][y] = '0'
    return x, y


N, M, x, y, K = map(int, input().split())
board = [list(input().split()) for _ in range(N)]
direc = list(input().split())
# 위 앞 아래 뒤 동 서
dice = ['0', '0', '0', '0', '0', '0']
res = []
for i in direc:
    m, n = x, y
    x, y = go(x, y, i)
    if (m, n) != (x, y):
        res.append(dice[0])
print('\n'.join(res))
