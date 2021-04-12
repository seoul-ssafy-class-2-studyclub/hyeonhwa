n = int(input())
a = list(map(int, input().split()))
dp = [0]*n
for i in range(n):
    value = 0
    for j in range(i):
        if a[i] < a[j]:
            value = max(value, dp[j])
    dp[i] = value + 1
print(max(dp))
