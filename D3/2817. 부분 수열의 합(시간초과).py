T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    # for i in range(1<<N):
    #     s = []
    #     for j in range(N):
    #         if i & (1<<j):
    #             s += [A[j]]
    #     if sum(s) == K:
    #         cnt += 1
    a = list(powerset(A))
    for i in a:
        if sum(i) == K:
            cnt += 1
    print('#{} {}'.format(t+1, cnt))
