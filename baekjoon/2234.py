from collections import deque
from pprint import pprint
def direction(n):
    if n == 0:
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if n == 1:
        return [(-1, 0), (1, 0), (0, 1)]
    if n == 3:
        return [(1, 0), (0, 1)]
    if n == 5:
        return [(-1, 0), (1, 0)]
    if n == 9:
        return [(-1, 0), (0, 1)]
    if n == 7:
        return [(1, 0)]
    if n == 11:
        return [(0, 1)]
    if n == 13:
        return [(-1, 0)]
    if n == 15:
        return []
    if n == 2:
        return [(1, 0), (0, -1), (0, 1)]
    if n == 6:
        return [(1, 0), (0, -1)]
    if n == 10:
        return [(0, -1), (0, 1)]
    if n == 14:
        return [(0, -1)]
    if n == 4:
        return [(-1, 0), (1, 0), (0, -1)]
    if n == 12:
        return [(-1, 0), (0, -1)]
    if n == 8:
        return [(-1, 0), (0, 1), (0, -1)]


def findroom(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        idx = direction(wall[x][y])
        for dx, dy in idx:
            if 0 <= x+dx < m and 0 <= y+dy < n and rooms[x+dx][y+dy] == 0 and (-dx, -dy) in direction(wall[x+dx][y+dy]):
                rooms[x+dx][y+dy] = cnt
                queue.append((x+dx, y+dy))


def close(x, y):
    global wrs
    wr = 1
    arr = [(x, y)]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < m and 0 <= y+dy < n and rooms[x][y] == rooms[x+dx][y+dy] and (x+dx, y+dy) not in arr:
                arr.append((x+dx, y+dy))
                wr += 1
                queue.append((x+dx, y+dy))
            elif 0 <= x+dx < m and 0 <= y+dy < n and rooms[x][y] != rooms[x+dx][y+dy] and rooms[x+dx][y+dy] not in wide[cnt]:
                wide[cnt].append(rooms[x+dx][y+dy])
    wrs.append(wr)


n, m = map(int, input().split())
wall = [list(map(int, input().split())) for _ in range(m)]
rooms = [[0]*n for _ in range(m)]
cnt = 1
initial = []
for i in range(m):
    for j in range(n):
        if rooms[i][j] == 0:
            initial.append((i, j))
            rooms[i][j] = cnt
            findroom(i, j)
            cnt += 1
room_count = cnt-1
if cnt-1 == m*n:
    if m == 1 and n == 1:
        before_wr = 1
        after_wr = 1
    else:
        before_wr = 1
        after_wr = 2
else:
    wrs = [0]
    wide = [[] for _ in range(cnt)]
    idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 1
    for i, j in initial:
        close(i, j)
        cnt += 1
    before_wr = max(wrs)
    after_wr = 0
    for i in range(1, cnt):
        for j in wide[i]:
            r = wrs[i] + wrs[j]
            if after_wr < r:
                after_wr = r
print(room_count)
print(before_wr)
print(after_wr)
