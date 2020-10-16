from collections import deque

def take(sx, sy):
    if board[sx][sy] > 1:
        temp, board[sx][sy] = board[sx][sy], 0
        return (temp, 0, sx, sy)
    visit = [[0]*n for _ in range(n)]
    visit[sx][sy] = 1
    queue = deque()
    queue.append((sx, sy, 0))
    customer = []
    while queue:
        x, y, cnt = queue.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < n and 0 <= y+dy < n and visit[x+dx][y+dy] == 0:
                if board[x+dx][y+dy] == 0:
                    queue.append((x+dx, y+dy, cnt+1))
                    visit[x+dx][y+dy] = 1
                elif board[x+dx][y+dy] > 1:
                    queue.append((x+dx, y+dy, cnt+1))
                    customer.append((board[x+dx][y+dy], cnt+1, x+dx, y+dy))
                    visit[x+dx][y+dy] = 1
                    if len(customer) == m:
                        customer.sort(key=lambda x:(x[1], x[2], x[3]))
                        board[customer[0][2]][customer[0][3]] = 0
                        return customer[0]
    return (0, -1, 0, 0)


def drop(sx, sy, ex, ey):
    if sx == ex and sy == ey:
        return (sx, sy, 0)
    visit = [[0]*n for _ in range(n)]
    visit[sx][sy] = 1
    queue = deque()
    queue.append((sx, sy, 0))
    while queue:
        x, y, cnt = queue.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < n and 0 <= y+dy < n and visit[x+dx][y+dy] == 0:
                if x+dx == ex and y+dy == ey:
                    return (x+dx, y+dy, cnt+1)
                if board[x+dx][y+dy] != 1:
                    queue.append((x+dx, y+dy, cnt+1))
                    visit[x+dx][y+dy] = 1
    return (0, 0, -1)


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1
final = {}
for i in range(2, m+2):
    a, b, c, d = map(int, input().split())
    board[a-1][b-1] = i
    final[i] = (c-1, d-1)
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = k
while m:
    customer_num, cost, sx, sy = take(sx, sy)
    if cost >= res or cost == -1:
        res = -1
        break
    ex, ey = final[customer_num]
    res -= cost
    sx, sy, cost = drop(sx, sy, ex, ey)
    if cost > res or cost == -1:
        res = -1
        break
    m -= 1
    res += cost
print(res)