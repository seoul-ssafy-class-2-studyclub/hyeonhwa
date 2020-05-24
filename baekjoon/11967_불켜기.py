import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
can = {}
for _ in range(m):
    x, y, a, b = map(int, input().split())
    if can.get((x, y)):
        can[(x, y)].append((a, b))
    else:
        can[(x, y)] = [(a, b)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visit = [[0]*(n+1) for _ in range(n+1)]
visit[1][1] = 1
go = [(1, 1)]
if can.get((1, 1)):
    go.extend(can[(1, 1)])
queue = [(1, 1)]
res = 0
for x, y in queue:
    for dx, dy in idx:
        if 1 <= x+dx <= n and 1 <= y+dy <= n and visit[x+dx][y+dy] == 0 and (x+dx, y+dy) in go:
            queue.append((x+dx, y+dy))
            visit[x+dx][y+dy] = 1
            if can.get((x+dx, y+dy)):
                go.extend(can[(x+dx, y+dy)])
                for i, j in can[(x+dx, y+dy)]:
                    for xx, yy in idx:
                        if 1 <= i+xx <= n and 1 <= j+yy <= n and (i+xx, j+yy) in queue:
                            queue.append((i, j))
                            if can.get((i, j)):
                                go.extend(can[(i, j)])
print(len(set(go)))
