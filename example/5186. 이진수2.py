def c2(x):
    a = []
    while x:
        m = x*2
        if m - 1 >= 0:
            a.append(1)
            x = x*2-1
        else:
            a.append(0)
            x = x*2
        if len(a) > 12:
            return 'overflow'
    return ''.join(list(map(str, a)))


T = int(input())
for t in range(T):
    N = float(input())
    res = c2(N)
    print('#{} {}'.format(t+1, res))