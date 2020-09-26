import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
board = [[1e10]*n for _ in range(n)]
for x in range(n):
    board[x][x] = 0
x, y = 0, 0
while x != -1 and y != -1:
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
    board[y-1][x-1] = 1

for z in range(n):
    for x in range(n):
        for y in range(n):
            if board[x][y] > board[x][z] + board[z][y]:
                board[x][y] = board[x][z] + board[z][y]
res = 1e10
s = []
for i in range(n):
    if res > max(board[i]):
        res = max(board[i])
        s = [i+1]
    elif res == max(board[i]):
        s.append(i+1)
print(res, len(s))
print(' '.join(list(map(str, s))))