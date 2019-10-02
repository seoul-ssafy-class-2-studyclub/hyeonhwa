# import sys
# sys.stdin = open('input5.txt', 'r')
def ax(arr, k, rs=0, s=0, x=0):
    global dp
    if x < M and s <= C:
        temp = rs+(arr[x]**2)
        ss = s+arr[x]
        if ss <= C:
            ax(arr, k, temp, ss, x+1)
            if temp > dp[k][0]:
                dp[k][0] = temp
        ax(arr, k, rs, s, x+1)


def cal(arr):
    k = 0
    for i in range(N):
        for j in range(N):
            if 0 <= j+M <= N:
                x = dp[k][0]
                ax(arr[i][j:j+M], k)
                if x != dp[k][0]:
                    dp[k][1] = i
                    dp[k][2] = j
            k += 1

T = int(input())
for t in range(T):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0, 0, 0] for _ in range(N**2)]
    cal(honey)
    dp.sort(key=lambda x:x[0], reverse=True)
    res = 0
    # print(dp)
    for i in range(5):
        if dp[1][1] != dp[0][1]:
            res = dp[0][0] + dp[1][0]
            break
        for j in range(i+1, 5):
            if dp[i][1] != dp[j][1]:
                if res < dp[i][0] + dp[j][0]:
                    res = dp[i][0] + dp[j][0]
            if dp[i][1] == dp[j][1] and (dp[i][2] >= dp[j][2]+M or dp[i][2]+M <= dp[j][2]):
                if dp[i][0]+dp[j][0] > res:
                    res = dp[i][0] + dp[j][0]
    print('#{} {}'.format(t+1, res))