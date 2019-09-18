T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    board = sorted(board, key=lambda x:x[1])
    res = []
    for x in board:
        if not res:
            res.append(x)
        else:
            if res[-1][0] == x[0]:
                if res[-1][1] > x[1]:
                    res[-1] = x
            else:
                if res[-1][1] <= x[0]:
                    res.append(x)
    print('#{} {}'.format(t+1, len(res)))
