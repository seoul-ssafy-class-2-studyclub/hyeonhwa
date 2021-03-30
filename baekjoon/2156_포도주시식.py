n = int(input())
amount = [int(input()) for _ in range(n)]
dp = [0]*n
dp[0] = amount[0]
if n > 1:
    dp[1] = max(amount[0] + amount[1], amount[1])
if n > 2:
    dp[2] = max(dp[1], amount[1] + amount[2], amount[0] + amount[2])
for i in range(3, n):
    dp[i] = max(dp[i-2] + amount[i], dp[i-3] + amount[i-1] + amount[i], dp[i-1])
print(max(dp))