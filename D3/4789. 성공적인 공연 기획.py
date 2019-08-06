T = int(input())
for t in range(T):
    N = list(map(int, input()))
    cnt, n = 0, []

    for i in range(1,len(N)):
        if N[i] == 0:
            n += [i-1]
        N[i] += N[i-1]
    for j in range(len(N)-1):
        if j+1 > N[j] and j not in n:
            cnt += j+1 - N[j]
        N[j+1] += cnt
    print('#{} {}'.format(t+1, cnt))
