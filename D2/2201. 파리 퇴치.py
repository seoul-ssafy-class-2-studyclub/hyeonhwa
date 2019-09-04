def kill(x, y):
    s = 0
    for i in range(M):
        s += sum(board[x+i][y:y+M])
    return s

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    s = 0
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            x = kill(i, j)
            if s < x:
                s = x
    print('#{} {}'.format(t+1, s))
            