import sys
input = lambda: sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
board = [[0]*m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = 0
for x in range(n):
    for y in range(m):
        if board[x][y] == 1:
            queue = [(x, y)]
            board[x][y] = -1
            amount = 1
            while queue:
                a, b = queue.pop()
                for dx, dy in idx:
                    if 0 <= a+dx < n and 0 <= b+dy < m and board[a+dx][b+dy] == 1:
                        queue.append((a+dx, b+dy))
                        board[a+dx][b+dy] = -1
                        amount += 1
            res = max(res, amount)
print(res)
