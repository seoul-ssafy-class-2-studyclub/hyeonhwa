import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

n, m = map(int, input().split())
male = [int(i) for i in input().split()]
wm = [int(i) for i in input().split()]
dp = [[INF]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 0
for i in range(m+1):
    dp[0][i] = 0
male.sort()
wm.sort()
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j-1] + abs(male[i-1] - wm[j-1])
        if i > j:
            dp[i][j] = min(dp[i][j], dp[i-1][j])
        elif i < j:
            dp[i][j] = min(dp[i][j], dp[i][j-1])
print(dp[n][m])