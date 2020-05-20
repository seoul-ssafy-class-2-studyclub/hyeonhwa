import sys
input = lambda: sys.stdin.readline().rstrip()

def bfs(start):
    queue = [start]
    for x, y, z, t in queue:
        for dx, dy, dz in idx:
            if 0 <= x+dx < l and 0 <= y+dy < r and 0 <= z+dz < c and visit[x+dx][y+dy][z+dz] == 0 and builings[x+dx][y+dy][z+dz] == '.':
                visit[x+dx][y+dy][z+dz] = 1
                queue.append((x+dx, y+dy, z+dz, t+1))
            elif 0 <= x+dx < l and 0 <= y+dy < r and 0 <= z+dz < c and builings[x+dx][y+dy][z+dz] == 'E':
                return t+1
    return -1

idx = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    builings = [[[i for i in input()]for _ in range(r+1)] for __ in range(l)]
    visit = [[[0]*c for _ in range(r)] for __ in range(l)]
    for x in range(l):
        for y in range(r):
            for z in range(c):
                if builings[x][y][z] == 'S':
                    start = (x, y, z, 0)
    res = bfs(start)
    if res == -1:
        print('Trapped!')
    else:
        print(f'Escaped in {res} minute(s).')
