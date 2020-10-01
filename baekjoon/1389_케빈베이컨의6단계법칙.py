import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
board = [[1e10]*n for _ in range(n)]
for i in range(n):
    board[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
    board[b-1][a-1] = 1
for z in range(n):
    for x in range(n):
        for y in range(n):
            if board[x][y] > board[x][z] + board[z][y]:
                board[x][y] = board[x][z] + board[z][y]
res = 0
total = 1e10
for i in range(n):
    if total > sum(board[i]):
        total = sum(board[i])
        res = i+1
print(res)