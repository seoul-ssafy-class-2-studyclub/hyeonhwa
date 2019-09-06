def check(arr):
    for i in range(9):
        if sum(arr[i]) != 45:
            return 0
        j = 0
        s = 0
        while j < 9:
            s += arr[j][i]
            j += 1
        if s != 45:
            return 0
    x = 0
    while x <= 6:
        s, l, r = 0, 0, 0
        for i in range(3):
            for j in range(3):
                s += arr[i+x][j+x]
                l += arr[i][j+x]
                r += arr[i+x][j]
        if s != 45 or l != 45 or r != 45:
            return 0
        x += 3
    return 1


T = int(input())
for t in range(T):
    board = [list(map(int, input().split())) for _ in range(9)]
    res = check(board)
    print('#{} {}'.format(t+1, res))
