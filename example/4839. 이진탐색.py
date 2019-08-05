T = int(input())
for t in range(T):
    P, Pa, Pb = list(map(int,input().split()))
    l, r, c, cnt_a, cnt_b = 1, P, 0, 0, 0
    while True:
        if c == Pa:
            break
        c = int((l+r)/2)
        cnt_a += 1
        if Pa > c:
            l = c
        else:
            r = c
    l, r = 1, P
    while True:
        if c == Pb:
            break
        c = int((l+r)/2)
        cnt_b += 1
        if Pb > c:
            l = c
        else:
            r = c
    print('#{}'.format(t+1), end=' ')
    if cnt_a < cnt_b:
        print('A')
    elif cnt_b < cnt_a:
        print('B')
    else:
        print(0)
