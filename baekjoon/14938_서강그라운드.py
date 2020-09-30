import sys
input = lambda: sys.stdin.readline().rstrip()

n, m, r = map(int, input().split())
board = [[1e10]*(n+1) for _ in range(n+1)]
items = list(map(int, input().split()))
for __ in range(r):
    a, b, l = map(int, input().split())
    board[a][b] = l
    board[b][a] = l
for i in range(1, n+1):
    board[i][i] = 0
for z in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            if board[x][y] > board[x][z] + board[z][y]:
                board[x][y] = board[x][z] + board[z][y]
res = 0
for i in range(1, n+1):
    total = items[i-1]
    for j in range(1, n+1):
        if i != j and board[i][j] <= m:
            total += items[j-1]
    res = max(res, total)
print(res)