T = int(input())
for t in range(T):
    board = [[i for i in input()]for _ in range(5)]
    l = len(board[0])
    for i in board[1:]:
        if len(i) > l:
            l = len(i)
    for i in board:
        if len(i) != l:
            i.extend([-1]*(l-len(i)))
    res = []
    for i in range(l):
        for j in range(5):
            if board[j][i] != -1:
                res += [board[j][i]]
    print('#{} {}'.format(t+1, ''.join(res)))