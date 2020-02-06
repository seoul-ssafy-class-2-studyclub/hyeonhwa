from pprint import pprint
import copy
import sys
sys.setrecursionlimit(90000)

def melt():
    melting = []
    for x in range(N):
        for y in range(M):
            if board[x][y] == 0:
                continue
            cnt = 0
            for dx, dy in idx:
                if 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] == 0:
                    cnt += 1
            melting.append((x, y, cnt))
    flag = False
    for x, y, cnt in melting:
        board[x][y] -= cnt
        if board[x][y] < 0:
            board[x][y] = 0
        elif board[x][y] > 0:
            flag = True
    return flag

def group():
    cnt = 1
    arr = [[0]*M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if board[x][y] > 0 and arr[x][y] == 0:
                if cnt == 2:
                    return False
                queue = [(x, y)]
                arr[x][y] = cnt
                while queue:
                    x, y = queue.pop()
                    for dx, dy in idx:
                        if 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] > 0 and arr[x+dx][y+dy] == 0:
                            arr[x+dx][y+dy] = cnt
                            queue.append((x+dx, y+dy))
                cnt += 1
    return True

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visit = [[0 for _ in range(M)] for __ in range(N)]

idx = [[0, 1], [1, 0], [0, -1], [-1, 0]]
year = 0

while True:
    res = melt()
    year += 1