from copy import deepcopy
import sys

sys.setrecursionlimit(10000)

def up(x, y):
    global cnt
    dx, dy = idx['U']
    while 0 <= x+dx < M and 0 <= y < N and universe[x+dx][y+dy] == '.':
        universe[x+dx][y+dy] = '*'
        cnt += 1
        up(x+dx, y+dy)
    if 0 <= x+dx < M and 0<= y < N and universe[x+dx][y+dy] == 'C':
        return 0
    elif 0 <= x+dx < M and 0<= y < N and universe[x+dx][y+dy] == '/':
        cnt += 1
        right(x+dx, y+dy)
    elif 0 <= x+dx < M and 0<= y < N and universe[x+dx][y+dy] == '\\':
        cnt += 1
        left(x+dy, y+dy)


def down(x, y):
    global cnt
    dx, dy = idx['D']
    while 0 <= x+dx < M and 0 <= y+dy < N and universe[x+dx][y+dy] == '.':
        universe[x+dx][y+dy] = '*'
        cnt += 1
        down(x+dx, y+dy)
    if 0 <= x+dx < M and 0<= y+dy < N and universe[x+dx][y+dy] == 'C':
        return 0
    elif 0 <= x+dx < M and 0<= y+dy < N and universe[x+dx][y+dy] == '/':
        cnt += 1
        left(x+dx, y+dy)
    elif 0 <= x+dx < M and 0<= y+dy < N and universe[x+dx][y+dy] == '\\':
        cnt += 1
        right(x+dx, y+dy)


def left(x, y):
    global cnt
    dx, dy = idx['L']
    while 0 <= x+dx < M and 0 <= y+dy < N and universe[x+dx][y+dy] == '.':
        universe[x+dx][y+dy] = '*'
        cnt += 1
        left(x+dx, y+dy)
    if 0 <= x+dx < M and 0<= y+dy < N and universe[x+dx][y+dy] == 'C':
        return 0
    elif 0 <= x+dx < M and 0<= y+dy < N and universe[x+dx][y+dy] == '/':
        cnt += 1
        down(x+dx, y+dy)
    elif 0 <= x+dx < M and 0<= y+dy < N and universe[x+dx][y+dy] == '\\':
        cnt += 1
        up(x+dx, y+dy)


def right(x, y):
    global cnt
    dx, dy = idx['R']
    while 0 <= x+dx < M and 0 <= y+dy < N and universe[x+dx][y+dy] == '.':
        universe[x+dx][y+dy] = '*'
        cnt += 1
        right(x+dx, y+dy)
    if 0 <= x+dx < M and 0<= y+dy < N and universe[x+dx][y+dy] == 'C':
        return 0
    elif 0 <= x+dx < M and 0<= y+dy < N and universe[x+dx][y+dy] == '/':
        cnt += 1
        up(x+dx, y+dy)
    elif 0 <= x+dx < M and 0<= y+dy < N and universe[x+dx][y+dy] == '\\':
        cnt += 1
        down(x+dx, y+dy)


N, M = map(int, input().split())
universes = [[i for i in input()] for _ in range(N)]
universe = deepcopy(universes)
pr, pc = map(int, input().split()) # universe[pc][pr]
universe[pc-1][pr-1] = '*'
idx = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}
cnt = 1
up(pc-1, pr-1)
maxtime = cnt
cnt = 1
universe = deepcopy(universes)
down(pc-1, pr-1)
if cnt > maxtime:
    maxtime = cnt
cnt = 1
universe = deepcopy(universes)
right(pc-1, pr-1)
if cnt > maxtime:
    maxtime = cnt
cnt = 1
universe = deepcopy(universes)
left(pc-1, pr-1)
if cnt > maxtime:
    maxtime = cnt
print(maxtime)
