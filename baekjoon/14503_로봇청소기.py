def search(x, y, d, board):
    res = 0
    while True:
        i, j = x, y
        if board[x][y] != -1:
            board[x][y] = -1
            res += 1
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
    return res


N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# for i in range(1, 5): (d-i)%4
idx = [[(0, -1), (1, 0), (0, 1), (-1, 0)], [(-1, 0), (0, -1), (1, 0), (0, 1)], [(0, 1), (-1, 0), (0, -1), (1, 0)], [(1, 0), (0, 1), (-1, 0), (0, -1)]]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
print(search(r, c, d, board))
