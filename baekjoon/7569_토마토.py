import sys
input = lambda: sys.stdin.readline().rstrip()

m, n, h = map(int, input().split())
tomatos = [[list(map(int, input().split())) for _ in range(n)] for __ in range(h)]
idx = [(1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0)]
ripe = []
cnt = 0
for x in range(h):
    for y in range(n):
        for z in range(m):
            if tomatos[x][y][z] == 0:
                cnt += 1
            elif tomatos[x][y][z] == 1:
                ripe.append((x, y, z, 0))
for x, y, z, day in ripe:
    for dx, dy, dz in idx:
        if 0 <= x+dx < h and 0 <= y+dy < n and 0 <= z+dz < m and tomatos[x+dx][y+dy][z+dz] == 0:
            tomatos[x+dx][y+dy][z+dz] = 1
            cnt -= 1
            ripe.append((x+dx, y+dy, z+dz, day+1))
if cnt:
    day = -1
print(day)
