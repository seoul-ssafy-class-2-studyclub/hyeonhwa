def makeone():
    one = [0]*(n**2)
    board_idx = 0
    ind = 0
    visit = [[0]*n for _ in range(n)]
    x, y = 0, 0
    visit[x][y] = 1
    while not (x == n//2 and y == n//2):
        dx, dy = idx[orders[ind]]
        if 0 <= x+dx < n and 0 <= y+dy < n and not visit[x+dx][y+dy]:
            one[board_idx] = board[x][y]
            x += dx
            y += dy
            visit[x][y] = 1
            board_idx += 1
        else:
            ind = (ind+1)%4
    return one


def blockpop(one):
    while True:
        flag = 0
        for _ in range(one.count(0)):
            one.remove(0)
        cnt = 1
        for i in range(1, len(one)):
            if one[i] == one[i-1]:
                cnt += 1
            else:
                if cnt >= 4:
                    res[one[i-1]] += cnt
                    for j in range(i-cnt, i):
                        one[j] = 0
                    flag = 1
                cnt = 1
        if cnt >= 4:
            res[one[-1]] += cnt
            one = one[:len(one)-cnt]
            flag = 1
        if not flag:
            break
    return one


def makeboard():
    board_idx = 0
    ind = 0
    visit = [[0]*n for _ in range(n)]
    x, y = 0, 0
    visit[x][y] = 1
    while not (x == n//2 and y == n//2):
        dx, dy = idx[orders[ind]]
        if 0 <= x+dx < n and 0 <= y+dy < n and not visit[x+dx][y+dy]:
            board[x][y] = one[board_idx]
            x += dx
            y += dy
            visit[x][y] = 1
            board_idx += 1
        else:
            ind = (ind+1)%4

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
idx = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
orders = [4, 2, 3, 1]
res = [0, 0, 0, 0]
for _ in range(m):
    d, s = map(int, input().split())
    dx, dy = idx[d]
    cnt = 0
    x, y = n//2, n//2
    while cnt < s:
        if 0 <= x+dx < n and 0 <= y+dy < n:
            x += dx
            y += dy
            board[x][y] = 0
        cnt += 1
    one = makeone()
    one = blockpop(one)
    re_one = []
    cnt = 1
    for i in range(1, len(one)):
        if one[i] == one[i-1]:
            cnt += 1
        else:
            re_one.extend([one[i-1], cnt])
            cnt = 1
    if one:
        re_one.extend([one[-1], cnt])
    one = re_one
    if len(one) >= n**2-1:
        one = one[len(one)-(n**2-1):]
    zero = [0]*(n**2-len(one)-1)
    one = zero + one
    makeboard()
ans = 0
for i in range(1, 4):
    ans += i*res[i]
print(ans)
