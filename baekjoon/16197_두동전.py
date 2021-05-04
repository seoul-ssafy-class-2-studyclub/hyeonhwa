def can(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False


def sol(i, j, ii, jj):
    queue = [(i, j, ii, jj, 0)]
    visit[i][j][ii][jj] = 1
    while queue:
        x1, y1, x2, y2, t = queue.pop(0)
        if t >= 10:
            return -1
        for dx, dy in idx:
            newx1, newy1, newx2, newy2 = x1, y1, x2, y2
            if can(x1+dx, y1+dy) and can(x2+dx, y2+dy):
                if board[x1+dx][y1+dy] != '#':
                    newx1 += dx
                    newy1 += dy
                if board[x2+dx][y2+dy] != '#':
                    newx2 += dx
                    newy2 += dy
                if not visit[newx1][newy1][newx2][newy2]:
                    queue.append((newx1, newy1, newx2, newy2, t+1))
                    visit[newx1][newy1][newx2][newy2] = 1
            elif (can(x1+dx, y1+dy) and not can(x2+dx, y2+dy)) or (not can(x1+dx, y1+dy) and can(x2+dx, y2+dy)):
                return t+1
    return -1


n, m = map(int, input().split())
board = [[i for i in input()] for _ in range(n)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
i, j, ii, jj = -1, -1, -1, -1
for x in range(n):
    for y in range(m):
        if board[x][y] == 'o':
            if i == -1:
                i, j = x, y
            else:
                ii, jj = x, y
                break
    if ii != -1:
        break
visit = [[[[False]*m for _ in range(n)] for __ in range(m)] for ___ in range(n)]
res = sol(i, j, ii, jj)
print(res)
