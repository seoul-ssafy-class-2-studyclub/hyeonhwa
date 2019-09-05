from pprint import pprint

def move(arr):
    if S == 'up':
        dx = -1
        for i in range(1, N):
            for j in range(N):
                x, y = i, j
                while 0 <= x+dx < N and board[x+dx][y][0] == 0:
                    board[x+dx][y][0] = board[x][y][0]
                    board[x][y][0] = 0
                    x += dx
                if 0 <= x+dx < N and board[x+dx][y][1] != 1 and board[x][y][1] != 1 and board[x+dx][y][0] == board[x][y][0]:
                    board[x+dx][y][0] += board[x][y][0]
                    board[x][y][0] = 0
                    board[x+dx][y][1] = 1
    elif S == 'down':
        dx = 1
        for i in range(N-2, -1, -1):
            for j in range(N):
                x, y = i, j
                while 0 <= x+dx < N and board[x+dx][y][0] == 0:
                    board[x+dx][y][0] = board[x][y][0]
                    board[x][y][0] = 0
                    x += dx
                if 0 <= x+dx < N and board[x+dx][y][1] != 1 and board[x][y][1] != 1 and board[x+dx][y][0] == board[x][y][0]:
                    board[x+dx][y][0] += board[x][y][0]
                    board[x][y][0] = 0
                    board[x+dx][y][1] = 1
    elif S == 'left':
        dy = -1
        for i in range(N):
            for j in range(1, N):
                x, y = i, j
                while 0 <= y+dy < N and board[x][y+dy][0] == 0:
                    board[x][y+dy][0] = board[x][y][0]
                    board[x][y][0] = 0
                    y += dy
                if 0 <= y+dy < N and board[x][y+dy][1] != 1 and board[x][y][1] != 1 and board[x][y+dy][0] == board[x][y][0]:
                    board[x][y+dy][0] += board[x][y][0]
                    board[x][y][0] = 0
                    board[x][y+dy][1] = 1
    elif S == 'right':
        dy = 1
        for i in range(N):
            for j in range(N-2, -1, -1):
                x, y = i, j
                while 0 <= y+dy < N and board[x][y+dy][0] == 0:
                    board[x][y+dy][0] = board[x][y][0]
                    board[x][y][0] = 0
                    y += dy
                if 0 <= y+dy < N and board[x][y+dy][1] != 1 and board[x][y][1] != 1 and board[x][y+dy][0] == board[x][y][0]:
                    board[x][y+dy][0] += board[x][y][0]
                    board[x][y][0] = 0
                    board[x][y+dy][1] = 1


T = int(input())
for t in range(T):
    N, S = input().split()
    N = int(N)
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in board:
        for j in range(N):
            i[j] = [i[j], 0]
    move(board)
    newboard = [[j[0] for j in i] for i in board]
    print('#{}'.format(t+1))
    for i in newboard:
        print(' '.join(list(map(str, i))))