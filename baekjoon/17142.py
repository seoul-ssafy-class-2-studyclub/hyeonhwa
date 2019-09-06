from pprint import pprint

def findvirus(arr):
    virus = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                virus.append((i, j))
    return virus


def combination(arr=[], k=-1):
    if len(arr) == M:
        res.append(arr)
        return 0
    for i in range(k+1, len(virus)):
        combination(arr+[virus[i]], i)
    return res


def diffusion(arr):
    global cnt
    queue = arr
    while queue:
        for dx, dy in idx:
            if 0 <= x+dx < N and 0 <= y+dy < N and newboard[x+dx][y+dy] == 0:
               newboard[x+dx][y+dy] = -cnt
    

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
virus = findvirus(board)
res = []
combination()
result = 100000000000000000000
for i in res:
    newboard = [i[:] for i in board]
    print(res)
    cnt = 1        
    if result > cnt-1:
        result = cnt-1
print(result)