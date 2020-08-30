import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(a, b):
    queue = [(a, b)]
    while queue:
        x, y = queue.pop()
        for dx, dy in idx:
            if 0 <= x+dx < h and 0 <= y+dy < w and board[x+dx][y+dy] == '1':
                board[x+dx][y+dy] = -1
                queue.append((x+dx, y+dy))

idx = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
w, h = map(int, input().split())
while w and h:
    board = [list(input().split()) for _ in range(h)]
    res = 0
    for x in range(h):
        for y in range(w):
            if board[x][y] == '1':
                board[x][y] = -1
                dfs(x, y)
                res += 1
    print(res)
    w, h = map(int, input().split())