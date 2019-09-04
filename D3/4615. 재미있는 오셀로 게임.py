from pprint import pprint

def check(x, y):
    b = board[x][y]
    i, j = x, y
    for dx, dy in idx:
        x, y = i, j
        while 0 <= x+dx < N and 0 <= y+dy < N and board[x+dx][y+dy] != b and board[x+dx][y+dy] != 0:
            board[x+dx][y+dy] = b
            pprint(board)
            x += dx
            y += dy


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for __ in range(N)]
    board[N//2][N//2], board[N//2-1][N//2-1], board[N//2-1][N//2], board[N//2][N//2-1] = 2, 2, 1, 1
    idx = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    pprint(board)
    for _ in range(M):
        y, x, k = map(int, input().split())
        y -= 1
        x -= 1
        board[x][y] = k
        pprint(board)
        check(x, y)