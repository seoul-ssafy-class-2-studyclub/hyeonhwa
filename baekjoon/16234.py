def union(x, y):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in idx:
            while 0 <= x+dx < N and 0 <= y+dy < N and board[x+dx][y+dy] == 0 and L <= abs(country[x][y]-country[x+dx][y+dy]) <= R:
                board[x+dx][y+dy] = cnt
                m.append((x+dx, y+dy))
                queue.append((x+dx, y+dy))
    return cnt


def move():
    for i in res:
        l = len(i)
        s = 0
        for x, y in i:
            s += country[x][y]
        k = s//l
        for x, y in i:
            country[x][y] = k


N, L, R = map(int, input().split())
country = [list(map(int, input().split()))for _ in range(N)]
idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
final = 0
while True:
    board = [[0 for _ in range(N)] for __ in range(N)]
    res = []
    cnt = 1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                board[i][j] = cnt
                m = [(i, j)]
                a = union(i, j)
                res.append(m)
                cnt += 1
    move()
    if cnt-1 == N**2:
        break
    final += 1
print(final)
