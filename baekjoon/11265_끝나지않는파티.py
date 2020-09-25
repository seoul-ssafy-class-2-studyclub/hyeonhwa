import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for z in range(n):
    for x in range(n):
        for y in range(n):
            if board[x][y] > board[x][z] + board[z][y]:
                board[x][y] = board[x][z] + board[z][y]
for _ in range(m):
    a, b, c = map(int, input().split())
    if board[a-1][b-1] <= c:
        print('Enjoy other party')
    else:
        print('Stay here')