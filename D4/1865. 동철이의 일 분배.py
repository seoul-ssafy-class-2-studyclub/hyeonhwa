# import sys
# sys.stdin = open('동철이.txt', 'r')

def permutation(arr, result=1):
    global res
    if result <= res:
        return 0
    if len(arr) == N:
        if result > res:
            res = result
            return 0
    for idx in range(N):
        if visited[idx]:
            continue
        if board[len(arr)][idx]:
            visited[idx] = True
            permutation(arr+[board[len(arr)][idx]], result*(board[len(arr)][idx]/100))
            visited[idx] = False


T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    l = []
    res = 0
    permutation([])
    res *= 100
    print('#{} {}'.format(t+1, "%0.6f" % res))

# dp 해답
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     M = 1 << N
#     dp = [[0.0 for _ in range(M)] for _ in range(N)]
 
#     G = []
#     for i in range(N):
#         G.append(list(map(float, input().split())))
#         for j in range(N):
#             G[i][j] = G[i][j] / 100
 
#     for i in range(N):
#         dp[0][1 << i] = G[0][i]
 
#     for i in range(1, N):
#         for cur in range(1, M):
#             if dp[i - 1][cur] == 0:
#                 continue
 
#             for j in range(N):
#                 if cur & (1 << j) != 0 or G[i][j] == 0:
#                     continue
#                 nxt = cur | (1 << j)
#                 print(nxt)
#                 dp[i][nxt] = max(dp[i][nxt], dp[i - 1][cur] * G[i][j])
#     print(dp)
#     print("#%d %.6f" % (test_case, dp[N - 1][M - 1]*100))