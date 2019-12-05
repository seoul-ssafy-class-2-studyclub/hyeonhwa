def search(x, y, d, board):
    while True:
        i, j = x, y
        board[x][y] = -1
        for dx, dy in idx[d]:
            if 0 <= x+dx < N and 0 <= y+dy < N and board[x+dx][y+dy] == 0:
                x += dx
                y += dy
                d = directions.index((dx, dy))
                break
        if x == i and y == j:
            dx, dy = directions[d]
            if 0 <= x-dx < N and 0 <= y-dy < M and board[x-dx][y-dy] == -1:
                x -= dx
                y -= dy
            elif 0 <= x-dx < N and 0 <= y-dy < M and board[x-dx][y-dy] == 1:
                break


N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
idx = [[(0, -1), (1, 0), (0, 1), (-1, 0)], [(-1, 0), (0, -1), (1, 0), (0, 1)], [(0, 1), (-1, 0), (0, -1), (1, 0)], [(1, 0), (0, 1), (-1, 0), (0, -1)]]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0
flag = 0
search(r, c, d, board)
for x in range(N):
    for y in range(M):
        if board[x][y] == -1:
            cnt += 1
print(cnt)
