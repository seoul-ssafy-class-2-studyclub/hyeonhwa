import sys
sys.stdin = open('input.txt', 'r')

def find(x, y):
    global row
    global col
    board[x][y] = -1
    for dx, dy in idx:
        if 0 <= x+dx < N and 0 <= y+dy < N and board[x+dx][y+dy] > 0:
            if dx == 1 and dy == 0:
                row += 1
            elif dx == 0 and dy == 1:
                col += 1
            find(x+dx, y+dy)

T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    idx = [[1, 0], [0, 1]]
    res = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                row, col = 0, 0
                find(i, j)
                row += 1
                col = col // row + 1
                res += [[row, col]]
    res.sort(key=lambda x:x[0]*x[1])
    result = []
    for x in range(len(res)-1):
        if res[x][0] * res[x][1] == res[x+1][0] * res[x+1][1]:
            if res[x][0] < res[x+1][0]:
                result += [res[x][0], res[x][1]]
            else:
                res[x], res[x+1] = res[x+1], res[x]
                result += [res[x][0], res[x][1]]
        else:
            result += [res[x][0], res[x][1]]
    result += [res[-1][0], res[-1][1]]
    print('#{} {} {}'.format(t+1, len(res), ' '.join(map(str, result))))
        