# import sys
# sys.stdin = open('정사각형.txt', 'r')

def dp(i, j):
    cnt = 1
    flag = True
    while flag:
        flag = False
        visited[board[i][j]] = True
        for dx, dy in idx:
            if 0 <= i+dx < N and 0 <= j+dy < N and board[i][j]+1 == board[i+dx][j+dy]:
                i += dx
                j += dy
                if cache[board[i][j]]:
                    cnt += cache[board[i][j]]
                    return cnt
                cnt += 1
                flag = True
                break
    return cnt


T = int(input())
for t in range(T):
    N = int(input())
    n = N**2
    board = [list(map(int, input().split())) for _ in range(N)]
    idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [False] * (n+1)
    cache = [0] * (n+1)
    res = 0
    for i in range(N):
        for j in range(N):
            if not visited[board[i][j]] and res <= n - board[i][j]:
                cnt = dp(i, j)
                cache[board[i][j]] = cnt
                if res == cnt:
                    if board[i][j] < l:
                        l = board[i][j]
                elif cnt > res:
                    res = cnt
                    l = board[i][j]
    print('#{} {} {}'.format(t+1, l, res))
