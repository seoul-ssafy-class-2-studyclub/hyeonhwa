from pprint import pprint
import copy
import sys
sys.setrecursionlimit(90000)

def findzero(x, y):
    for [dx,dy] in idx:
        if 0 < x < N and 0 < y < M and board[x+dx][y+dy] == 0:
            arr[x][y] -= 1
            if arr[x][y] < 0:
                arr[x][y] = 0
                break
    return board


def findgroup(x, y):
    if board[x][y] > 0 and not visit[x][y]:
        visit[x][y] = cnt
    for [dx, dy] in idx:
        if board[x+dx][y+dy] > 0 and not visit[x+dx][y+dy]:
            visit[x+dx][y+dy] = cnt
            findgroup(x+dx, y+dy)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
arr = copy.deepcopy(board)

visit = [[0 for _ in range(M)] for __ in range(N)]

idx = [[0, 1], [1, 0], [0, -1], [-1, 0]]
cnt = 1
year = 0

while True:
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                findzero(i, j)
                if board[i][j] == 0:
                    findgroup(i, j)
    cnt += 1
    pprint(visit)
    if cnt >= 4:
        break

# # print()
# # pprint(visit)
# # pprint(board)