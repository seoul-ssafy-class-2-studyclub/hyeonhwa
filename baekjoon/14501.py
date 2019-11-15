N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*(N)
for i in range(N):
    for j in range(i+1):
        if l[i - j][0] <= j and i + l[i][0] <= N:
            dp[i] = max(dp[i], dp[i-j]+l[i][1])
    if dp[i] == 0 and i + l[i][0] <= N:
        dp[i] = l[i][1]
print(max(dp))
