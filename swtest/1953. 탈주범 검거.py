# import sys
# sys.stdin = open('탈주범.txt', 'r')

def direction(x, y):
    if board[x][y] == 1:
        idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    elif board[x][y] == 2:
        idx = [[-1, 0], [1, 0]]
    elif board[x][y] == 3:
        idx = [[0, -1], [0, 1]]
    elif board[x][y] == 4:
        idx = [[-1, 0], [0, 1]]
    elif board[x][y] == 5:
        idx = [[1, 0], [0, 1]]
    elif board[x][y] == 6:
        idx = [[1, 0], [0, -1]]
    elif board[x][y] == 7:
        idx = [[-1, 0], [0, -1]]
    return idx


def move(x, y, arr, visit, t=1):
    global k
    queue = [(x, y)]
    while queue:
        nxt = []
        for x, y in queue:
            for dx, dy in direction(x, y):
                if 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] > 0 and visit[x+dx][y+dy] == False:
                    for a, b in direction(x+dx, y+dy):
                        if 0 <= x+dx+a < N and 0 <= y+dy+b < M and x+dx+a == x and y+dy+b == y:
                            nxt.append((x+dx, y+dy))
                            visit[x+dx][y+dy] = True
                            k += 1
        queue = nxt
        t += 1
        if t == L:
            break


T = int(input())
for t in range(T):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False]*M for _ in range(N)]
    visit[R][C] = True
    k = 1
    if L == 1:
        print('#{} 1'.format(t+1))
    else:
        move(R, C, board, visit)
        print('#{} {}'.format(t+1, k))
