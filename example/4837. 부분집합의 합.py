T = int(input())
for t in range(T):
    N, K = list(map(int, input().split()))
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    result = []
    cnt = []
    for i in range(1<<len(A)):
        a = []
        for j in range(len(A)):
            if i & (1<<j):
                a.append(A[j])
        if len(a) == N:
            result.append(a)
    for i in result:
        if sum(i) == K:
            cnt += [i]
    if cnt == []:
        count = 0
    else:
        count = len(cnt)
    print('#{} {}'.format(t+1, count))
        