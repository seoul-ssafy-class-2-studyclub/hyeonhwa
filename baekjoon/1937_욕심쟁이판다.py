import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def check(a, b):
    if visit[a][b]:
        return visit[a][b]
    visit[a][b] = 1
    for dx, dy in idx:
        if 0 <= a+dx < n and 0 <= b+dy < n and forest[a][b] < forest[a+dx][b+dy]:
            visit[a][b] = max(visit[a][b], check(a+dx, b+dy)+1)
    return visit[a][b]


n = int(input())
forest = [[int(i) for i in input().split()] for _ in range(n)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visit = [[0]*n for _ in range(n)]
ans = 0
for x in range(n):
    for y in range(n):
        ans = max(ans, check(x, y))
print(ans)