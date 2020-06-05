import collections

def rotate():
    for i in range(N):
        if (i+1)%x == 0:
            m = 0
            while m < k:
                if d == 0:
                    circles[i].insert(0, circles[i].pop())
                else:
                    circles[i].append(circles[i].pop(0))
                m += 1


def rmsame(x, y):
    global s
    global flag
    queue = collections.deque()
    queue.append((x, y))
    l = [(x, y)]
    while queue:
        x, y = queue.pop()
        for dx, dy in idx:
            j = y
            if 0 <= x+dx < N and -1 <= y+dy <= M:
                if y+dy == -1:
                    j = M
                elif y+dy == M:
                    j = -1
                if circles[x][y] == circles[x+dx][j+dy] and (x+dx, j+dy) not in l:
                    queue.append((x+dx, j+dy))
                    l.append((x+dx, j+dy))
    if len(l) >= 2:
        flag = 1
        for i, j in l:
            circles[i][j] = 0


def avg():
    if ix != 0:
        average = s/ix
        for x in range(N):
            for y in range(M):
                if circles[x][y] != 0:
                    if circles[x][y] > average:
                        circles[x][y] -= 1
                    elif circles[x][y] < average:
                        circles[x][y] += 1


N, M, T = map(int, input().split())
circles = [list(map(int, input().split())) for _ in range(N)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(T):
    x, d, k = map(int, input().split())
    rotate()
    s = 0
    ix = 0
    flag = 0
    for i in range(N):
        for j in range(M):
            if circles[i][j] != 0:
                rmsame(i, j)
                if circles[i][j] != 0:
                    ix += 1
                    s += circles[i][j]
    if flag == 0:
        avg()
res = 0
for i in range(N):
    for j in range(M):
        res += circles[i][j]
print(res)
