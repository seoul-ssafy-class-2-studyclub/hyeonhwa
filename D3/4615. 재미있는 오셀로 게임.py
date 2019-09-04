def check(x, y):
    b = board[x][y]
    i, j = x, y
    for dx, dy in idx:
        x, y = i, j
        change = []
        while 0 <= x+dx < N and 0 <= y+dy < N and board[x+dx][y+dy] != b and board[x+dx][y+dy] != 0:
            change += [[x+dx, y+dy]] 
            x += dx
            y += dy
        if change and 0 <= change[-1][0]+dx < N and 0 <= change[-1][1]+dy < N and board[change[-1][0]+dx][change[-1][1]+dy] == b:
            for dx, dy in change:
                board[dx][dy] = b


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for __ in range(N)]
    board[N//2][N//2], board[N//2-1][N//2-1], board[N//2-1][N//2], board[N//2][N//2-1] = 2, 2, 1, 1
    idx = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    for _ in range(M):
        y, x, k = map(int, input().split())
        y -= 1
        x -= 1
        board[x][y] = k
        check(x, y)
    w, b= 0, 0
    for i in board:
        w += i.count(2)
        b += i.count(1)
    print('#{} {} {}'.format(t+1, b, w))
