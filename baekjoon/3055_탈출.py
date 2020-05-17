import sys
input = lambda: sys.stdin.readline().rstrip()

def bfs():
    cnt = 0
    visit = [[0]*c for _ in range(r)]
    visit[hedgehog[0][0]][hedgehog[0][1]] = 1
    while hedgehog:
        for _ in range(len(water)):
            x, y = water.pop(0)
            for dx, dy in idx:
                if 0 <= x+dx < r and 0 <= y+dy < c and (board[x+dx][y+dy] == '.' or board[x+dx][y+dy] == 'S'):
                    water.append((x+dx, y+dy))
                    board[x+dx][y+dy] = '*'
        for _ in range(len(hedgehog)):
            x, y = hedgehog.pop(0)
            for dx, dy in idx:
                if 0 <= x+dx < r and 0 <= y+dy < c:
                    if board[x+dx][y+dy] == 'D':
                        return cnt + 1
                    elif board[x+dx][y+dy] == '.' and visit[x+dx][y+dy] == 0:
                        visit[x+dx][y+dy] = 1
                        hedgehog.append((x+dx, y+dy))
        cnt += 1
    return 'KAKTUS'


r, c = map(int, input().split())
board = [[i for i in input()] for _ in range(r)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
water = []
for x in range(r):
    for y in range(c):
        if board[x][y] == '*':
            water.append((x, y))
        elif board[x][y] == 'S':
            hedgehog = [(x, y)]
res = bfs()
print(res)