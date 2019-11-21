N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
road = [[1]*N for _ in range(N)]
res = 0
# 플로이드 와샬
flag = 0
for z in range(N):
    for x in range(N):
        for y in range(N):
            if x == y or y == z or x == z:
                continue
            if board[x][y] > board[x][z] + board[z][y]:
                flag = 1
                res = -1
                break
            if board[x][y] == board[x][z] + board[z][y]:
                road[x][y] = 0
        if flag == 1:
            break
    if flag == 1:
        break
if res != -1:
    for x in range(N):
        for y in range(N):
            if road[x][y] == 1:
                res += board[x][y]
print(res//2)
