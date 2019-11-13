import sys
sys.stdin = open('파핑파핑.txt', 'r')
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    numboard[x][y] = -1
    while queue:
        x, y = queue.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < N and 0 <= y+dy < N and numboard[x+dx][y+dy] != '*' and numboard[x+dx][y+dy] != -1:
                if numboard[x+dx][y+dy] == 0:
                    queue.append((x+dx, y+dy))
                numboard[x+dx][y+dy] = -1


for t in range(int(input())):
    N = int(input())
    board = [[i for i in input()] for _ in range(N)]
    idx = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    safes = []
    numboard = [[0 for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                cnt = 0
                for dx, dy in idx:
                    if 0 <= i+dx < N and 0 <= j+dy < N and board[i+dx][j+dy] == '*':
                        cnt += 1
                numboard[i][j] = cnt
            else:
                numboard[i][j] = '*'
    res = 0
    for x in range(N):
        for y in range(N):
            if numboard[x][y] == 0:
                bfs(x, y)
                res += 1
    for x in range(N):
        for y in range(N):
            if numboard[x][y] != -1 and numboard[x][y] != '*':
                res += 1
    print(f'#{t+1} {res}')
