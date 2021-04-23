from pprint import pprint

def sol(x, y, d, visit, board):
    flag = 0
    while True:
        visit[x][y] = 1
        # pprint(visit)
        if flag == 4:
            dx, dy = idx[d]
            if 0 <= x-dx < n and 0 <= y-dy < m and not board[x-dx][y-dy]:
                x -= dx
                y -= dy
                flag = 0
                continue
            else:
                break
        k = d-1
        if k < 0:
            k = 3
        dx, dy = idx[k]
        if 0 <= x+dx < n and 0 <= y+dy < m and not visit[x+dx][y+dy] and not board[x+dx][y+dy]:
            x += dx
            y += dy
            d -= 1
            if d < 0:
                d = 3
            flag = 0
        elif (0 <= x+dx < n and 0 <= y+dy < m and visit[x+dx][y+dy] and not board[x+dx][y+dy]) or (x+dx < 0 or x+dx >= n or y+dy < 0 or y+dy >= m) or (0 <= x+dx < n and 0 <= y+dy < m and board[x+dx][y+dy]):
            flag += 1
            d -= 1
            if d < 0:
                d = 3


n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
idx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visit = [[0]*m for _ in range(n)]
sol(r, c, d, visit, board)
res = 0
for i in range(n):
    res += visit[i].count(1)
print(res)
