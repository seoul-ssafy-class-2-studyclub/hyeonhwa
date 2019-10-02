import sys
sys.stdin = open('input4.txt', 'r')

T = int(input())
for t in range(T):
    money = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    dp = [0] * 12
    dp[0] = min(money[0]*plan[0], money[1])
    for i in range(1, 12):
        dp[i] = min(dp[i-1]+money[0]*plan[i], dp[i-1]+money[1])
        if i >= 2:
            dp[i] = min(dp[i-3]+money[2], dp[i])
    res = min(dp[11], money[3])
    print('#{} {}'.format(t+1, res))
    