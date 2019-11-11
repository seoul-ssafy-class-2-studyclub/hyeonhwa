def go(x, y, dx, dy, l):
    global res
    global flag
    cnt = 1
    while (dx and x < N-1) or (dy and y < N-1):
        if 0 <= x+dx < N and 0 <= y+dy < N and board[x][y] == board[x+dx][y+dy]:
            x += dx
            y += dy
            cnt += 1
        elif 0 <= x+dx < N and 0 <= y+dy < N and abs(board[x][y] - board[x+dx][y+dy]) == 1:
            if board[x][y] < board[x+dx][y+dy]:
                if cnt >= L:
                    x += dx
                    y += dy
                    cnt = 1
                else:
                    flag = 1
                    break
            else:
                cnt = 1
                x, y = x+dx, y+dy
                while 0 <= x+dx < N and 0 <= y+dy < N and board[x][y] == board[x+dx][y+dy] and cnt < L:
                    x += dx
                    y += dy
                    cnt += 1
                if cnt >= L:
                    cnt = 0
                else:
                    flag = 1
                    break
        elif 0 <= x+dx < N and 0 <= y+dy < N and board[x][y] != board[x+dx][y+dy] and abs(board[x][y] - board[x+dx][y+dy]) != 1:
            flag = 1
            break
    if flag == 1:
        return
    if (dx and x == N-1) or (dy and y == N-1):
        res += 1


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
res = 0
for x in range(N):
    flag = 0
    go(x, 0, 0, 1, [])

for y in range(N):
    flag = 0
    go(0, y, 1, 0, [])
print(res)
