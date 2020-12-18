n, k = map(int, input().split())
prime = [1]*(n+1)
prime[0], prime[1] = 0, 0
i = 2
cnt = 0
while i <= n:
    if prime[i]:
        cnt += 1
        if cnt == k:
            print(i)
            break
        for j in range(i*i, n+1, i):
            if prime[j]:
                prime[j] = 0
                cnt += 1
                if cnt == k:
                    print(j)
                    break
        if cnt == k:
            break
    i += 1
