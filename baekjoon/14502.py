from pprint import pprint

def diffusion(arr, x, y):
    stack = [x, y]
    while stack:
        y = stack.pop()
        x = stack.pop()
        for dx, dy in idx:
            while 0 <= x+dx < N and 0 <= y+dy < M and arr[x+dx][y+dy] == 0:
                arr[x+dx][y+dy] = 2
                stack.extend([x+dx, y+dy])


def findzero(arr):
    zero = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                zero += [[i, j]]
    return zero


def findvirus(arr):
    virus = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                virus += [[i, j]]
    return virus


def combination(arr=[], idx=-1):
    if len(arr) == 3:
        res.append(arr)
        return 0
    for i in range(idx+1, len(zero)):
        combination(arr+[zero[i]], i)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
zero = findzero(board)
virus = findvirus(board)
res = []
combination()
safety = 0
for x, y, z in res:
    newboard = [j[:] for j in board]
    newboard[x[0]][x[1]] = 1
    newboard[y[0]][y[1]] = 1
    newboard[z[0]][z[1]] = 1
    for i, j in virus:
        diffusion(newboard, i, j)
    s = 0
    for i in newboard:
        s += i.count(0)
    if s > safety:
        safety = s
print(safety)
