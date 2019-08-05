T = int(input())
if 1 <= T <= 50:
    for t in range(T):
        K, N, M = input().split()
        k = int(K)
        k2 = k
        n = int(N)
        m = list(map(int, input().split()))
        cnt, x = 0, 0
        for j in range(n):
            if k2 < n:
                for i in m:
                    if i <= k2: # 1, 3, 7 8 9 4 7 9 14 17
                        x = i
                cnt += 1
                k2 = x + k

            if cnt == n:
                cnt = 0

        print('#{} {}'.format(t+1,cnt))