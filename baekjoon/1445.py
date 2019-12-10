def go():
    pass

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
trash = [[0]*N for _ in range(M)]
neartrash = [[0]*N for _ in range(M)]
for x in range(N):
    for y in range(M):
        if board[x][y] == 'S':
            start = (x, y)
        elif board[x][y] == 'F':
            end = (x, y)
        elif board[x][y] == 'g':
            trash[x][y] = 1
            for dx, dy in idx:
                if 0 <= x+dx < N and 0 <= y+dy < M:
                    neartrash[x+dx][y+dy] = 1
