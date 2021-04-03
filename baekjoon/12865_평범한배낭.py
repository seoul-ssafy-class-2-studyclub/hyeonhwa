# DP의 대표적 문제!
n, k = map(int, input().split())
# 물건 개수 / 무게
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        if j >= w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]
print(max(dp[-1]))
