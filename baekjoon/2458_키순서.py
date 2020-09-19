import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
board = [[1e10]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            board[i][j] = 0
for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if board[j][k] > board[j][i] + board[i][k]:
                board[j][k] = board[j][i] + board[i][k]
res = 0
# print(board)
for i in range(1, n+1):
    flag = 0
    for j in range(1, n+1):
            if board[i][j] >= 1e10 and board[j][i] >= 1e10:
                flag = 1
                break
    if not flag:
        res += 1
print(res)