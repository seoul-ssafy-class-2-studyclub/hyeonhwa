def fac(n):
    global a
    for i in range(1,n+1):
        a += [a[i-1]*i]
    return a[n]

a = [1]

T = int(input())
for t in range(T):
    N = int(input())
    n = N // 20
    s = 1
    for i in range(1, n+1):
        cnt = N // 10 - i
        cnt = fac(cnt)/(fac(cnt-i)*fac(i))
        s += int(2**i * cnt)
    print('#{} {}'.format(t+1, s))
