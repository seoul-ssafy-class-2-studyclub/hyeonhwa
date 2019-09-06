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
        nxt = []
        flag = 0
        for x, y in queue:
            for dx, dy in idx:
                if 0 <= x+dx < N and 0 <= y+dy < N and newboard[x+dx][y+dy] == 0:
                    newboard[x+dx][y+dy] = -cnt
                    nxt.append((x+dx, y+dy))
                elif 0 <= x+dx < N and 0 <= y+dy < N and newboard[x+dx][y+dy] == 2:
                    for i in newboard:
                        if 0 in i:
                            flag = 1
                    if flag == 1:
                        newboard[x+dx][y+dy] = -cnt
                        nxt.append((x+dx, y+dy))
                    else:
                        break
        queue = nxt
        if nxt:
            cnt += 1
    for i in newboard:
        if 0 in i:
            return -1
    return cnt-1
    

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
virus = findvirus(board)
res = []
combination()
result = 1000000
for i in res:
    newboard = [i[:] for i in board]
    cnt = 1        
    x = diffusion(i)
    if x != -1 and result > x:
        result = x
if result == 1000000:
    result = -1
print(result)