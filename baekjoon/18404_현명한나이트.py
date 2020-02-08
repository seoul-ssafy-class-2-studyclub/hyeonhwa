import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
x, y = list(map(int, input().split()))
enemy = [tuple(map(int, input().split())) for _ in range(M)]
idx = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
visit = [[-1]*(N+1) for _ in range(N+1)]
visit[x][y] = 0
queue = [(x, y, 0)]
for x, y, z in queue:
    z += 1
    for dx, dy in idx:
        if 1 <= x+dx <= N and 1 <= y+dy <= N and visit[x+dx][y+dy] == -1:
            visit[x+dx][y+dy] = z
            queue.append((x+dx, y+dy, z))
print(*(visit[x][y] for x, y in enemy))
