for t in range(10):
    N = int(input())
    border = [[i for i in input().split()] for j in range(100)]
    k = border[99].index(2)
    for i in range(99, 0, -1):
        if k != 0 and border[i][k-1] == '1':
            while k > 0 and border[i][k-1] == '1':
                k -= 1
        elif k != 99 and border[i][k+1] == '1':
            while k < 99 and border[i][k+1] == '1':
                k += 1
    print('#{} {}'.format(t+1, k))