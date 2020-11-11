n, m = map(int, input().split())
prime = [1]*(m+1)
prime[0], prime[1] = 0, 0
i = 2
while i*i <= m:
    if prime[i]:
        for j in range(i*i, m+1, i):
            if prime[j]:
                prime[j] = 0
    i += 1
for i in range(n, m+1):
    if prime[i]:
        print(i)
