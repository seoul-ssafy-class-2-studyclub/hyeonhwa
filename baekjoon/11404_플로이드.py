import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

board = [[1e10]*n for _ in range(n)]
for __ in range(m):
    a, b, c = map(int, input().split())
    board[a-1][b-1] = min(board[a-1][b-1], c)
for i in range(n):
    board[i][i] = 0
for z in range(n):
    for x in range(n):
        for y in range(n):
            if board[x][y] > board[x][z] + board[z][y]:
                board[x][y] = board[x][z] + board[z][y]
for x in range(n):
    for y in range(n):
        if board[x][y] == 1e10:
            board[x][y] = 0
for i in range(n):
    print(' '.join(list(map(str, board[i]))))