from collections import deque

def go(a, b, k):
    dx, dy = idx[k]
    if 0 <= a-dx < n and 0 <= b-dy < n and visit[a-dx][b-dy][k]:
        visit[a][b][k] = visit[a-dx][b-dy][k]
        return visit[a][b][k]
    if (dx and (a+dx == -1 or a+dx == n)) or (dy and (b+dy == -1 or b+dy == n)):
        visit[a][b][k] = 1
        return visit[a][b][k]
    queue = deque()
    queue.append((a, b))
    cnt = 0
    i = k
    while queue:
        x, y = queue.pop()
        if (dx and (x+dx == -1 or x+dx == n)) or (dy and (y+dy == -1 or y+dy == n)):
            queue.append((x+dx, y+dy))
            dx, dy = -dx, -dy
            i = idx.index((dx, dy))
            cnt += 1
        elif 0 <= x+dx < n and 0 <= y+dy < n:
            if board[x+dx][y+dy] == 0:
                queue.append((x+dx, y+dy))
                if (x+dx, y+dy) == (a, b):
                    visit[a][b][k] = cnt
                    return visit[a][b][k]
                if (dx and (x+dx == 0 or x+dx == n-1)) or (dy and (y+dy == 0 or y+dy == n-1)):
                    dx, dy = -dx, -dy
                    i = idx.index((dx, dy))
                    cnt += 1
            elif board[x+dx][y+dy] == -1:
                visit[a][b][k] = cnt
                return visit[a][b][k]
            elif 1 <= board[x+dx][y+dy] <= 5:
                queue.append((x+dx, y+dy))
                dx, dy = reidx[board[x+dx][y+dy]][i]
                i = idx.index((dx, dy))
                cnt += 1
            else:
                h = holl[board[x+dx][y+dy]]
                for xx, yy in h:
                    if xx != x+dx or yy != y+dy:
                        queue.append((xx, yy))
                        break


for t in range(int(input())):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    holl = {}
    idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    reidx = {1:[(1, 0), (0, 1), (-1, 0), (0, -1)], 
            2:[(0, 1), (-1, 0), (1, 0), (0, -1)],
            3:[(0, -1), (-1, 0), (0, 1), (1, 0)],
            4:[(1, 0), (0, -1), (0, 1), (-1, 0)],
            5:[(1, 0), (-1, 0), (0, 1), (0, -1)]}
    for x in range(n):
        for y in range(n):
            if board[x][y] > 5:
                if holl.get(board[x][y]):
                    holl[board[x][y]].append((x, y))
                else:
                    holl[board[x][y]] = [(x, y)]
    visit = [[[0]*4 for _ in range(n)] for __ in range(n)]
    res = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                for i in range(4):
                    res = max(res, go(x, y, i))
    print(f'#{t+1} {res}')