import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(x, y):
    global res
    for idx in arr:
        flag = 0
        s = board[x][y]
        for dx, dy in idx:
            if 0 <= x+dx < n and 0 <= y+dy < m:
                s += board[x+dx][y+dy]
            else:
                flag = 1
                break
        if flag == 0:
            res = max(res, s)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
res = 0
arr = [[(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)], [(0, 1), (1, 0), (1, 1)], 
    [(1, 0), (2, 0), (2, 1)], [(1, 0), (2, 0), (2, -1)], [(0, 1), (0, 2), (1, 2)], [(0, 1), (0, 2), (-1, 2)], [(-1, 0), (-2, 0), (-2, 1)], [(-1, 0), (-2, 0), (-2, -1)], [(0, -1), (0, -2), (-1, -2)], [(0, -1), (0, -2), (1, -2)],
    [(1, 0), (1, 1), (2, 1)], [(1, 0), (1, -1), (2, -1)], [(0, 1), (-1, 1), (-1, 2)], [(0, 1), (1, 1), (1, 2)],
    [(0, -1), (0, 1), (1, 0)], [(-1, 0), (1, 0), (0, 1)], [(0, -1), (0, 1), (-1, 0)], [(-1, 0), (1, 0), (0, -1)]]
for x in range(n):
    for y in range(m):
        dfs(x, y)
print(res)