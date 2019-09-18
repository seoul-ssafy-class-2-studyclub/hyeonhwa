T = int(input())
for ts in range(T):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    s = 0
    while w and t:
        for i in w[:]:
            if i > max(t):
                w.remove(i)
        if w and t:
            s += max(w)
            w.remove(max(w))
            t.remove(max(t))
    if s > 0:
        print('#{} {}'.format(ts+1, s))
    else:
        print('#{} 0'.format(ts+1))