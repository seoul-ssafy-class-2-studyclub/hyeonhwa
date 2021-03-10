def solution(x):
    dp = [0]*11
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, x+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[x]

for _ in range(int(input())):
    n = int(input())
    print(solution(n))
