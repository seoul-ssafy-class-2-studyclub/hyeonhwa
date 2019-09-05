def findx(x, y):
    global cnt
    dx = 1
    k = 1
    while 0 <= x+dx < N and board[x][y] == 1 and board[x+dx][y] == board[x][y]:
        k += 1
        x += dx
        if 0 <= x+dx < N and board[x+dx][y] != board[x][y] and k == K:
            cnt += 1
        elif x == N-1 and k == K:
            cnt += 1
    if x+dx != N:
        findx(x+dx, y)


def findy(x, y):
    global cnt
    dy = 1
    k = 1
    while 0 <= y+dy < N and board[x][y] == 1 and board[x][y+dy] == board[x][y]:
        k += 1
        y += dy
        if 0 <= y+dy < N and board[x][y+dy] != 1 and k == K:
            cnt += 1
        elif y == N-1 and k == K:
            cnt += 1
    if y+dy != N:
        findy(x, y+dy)


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    board = [list(map(int, input().split()))for _ in range(N)]
    cnt = 0
    for i in range(N):
        findx(0, i)
        findy(i, 0)
    print('#{} {}'.format(t+1, cnt))
    