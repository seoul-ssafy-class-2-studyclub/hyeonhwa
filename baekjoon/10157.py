from pprint import pprint
import sys

sys.setrecursionlimit(10000)

def down(x, y):
    global cnt
    dx, dy = idx[2]
    while x+dx <= R and board[x][y] == 0:
        board[x][y] = cnt
        if cnt == K:
            res.extend([x+1, y+1])
        cnt += 1
        xy.extend([x, y])
        # pprint(board)
        down(x+dx, y+dy)


def up(x, y):
    global cnt
    dx, dy = idx[3]
    while x+dx >= -1 and board[x][y] == 0:
        board[x][y] = cnt
        if cnt == K:
            res.extend([x+1, y+1])
        cnt += 1
        xy.extend([x, y])
        # pprint(board)
        up(x+dx, y+dy)


def left(x, y):
    global cnt
    dx, dy = idx[1]
    while y+dy >= -1 and board[x][y] == 0:
        board[x][y] = cnt
        if cnt == K:
            res.extend([x+1, y+1])
        cnt += 1
        xy.extend([x, y])
        # pprint(board)
        left(x+dx, y+dy)


def right(x, y):
    global cnt
    dx, dy = idx[0]
    while y+dy <= C and board[x][y] == 0:
        board[x][y] = cnt
        if cnt == K:
            res.extend([x+1, y+1])
        cnt += 1
        xy.extend([x, y])
        # pprint(board)
        right(x+dx, y+dy)


C, R = map(int, input().split())
board = [[0 for _ in range(C)] for __ in range(R)]
K = int(input())
idx = [[0, 1], [0, -1], [1, 0], [-1, 0]]
cnt = 1
xy = [-1, 0]
res = []
while True:
    if C * R < K:
        print(0)
        break        
    x, y = xy[-2], xy[-1]
    down(x+1, y)
    if res:
        print(res[1], res[0])
        break
    x, y = xy[-2], xy[-1]
    right(x, y+1)
    if res:
        print(res[1], res[0])
        break
    x, y = xy[-2], xy[-1]
    up(x-1, y)
    if res:
        print(res[1], res[0])
        break
    x, y = xy[-2], xy[-1]
    left(x, y-1)
    if res:
        print(res[1], res[0])
        break
    x, y = xy[-2], xy[-1]
    k = 0
    for i in board:
        if 0 not in i:
            k += 1
    if k == len(board):
        break