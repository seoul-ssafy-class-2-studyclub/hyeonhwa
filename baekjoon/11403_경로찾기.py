import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
board = [list(input().split()) for _ in range(n)]

for z in range(n):
    for x in range(n):
        for y in range(n):
            if board[x][y] == '0' and board[x][z] == '1' and board[z][y] == '1':
                board[x][y] = '1'
for i in range(n):
    print(' '.join(board[i]))