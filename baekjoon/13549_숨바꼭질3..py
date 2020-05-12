import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
if n == k: res = 0
else:
    queue = deque()
    queue.append((n, 0))
    visit = [1e9 for _ in range(200001)]
    res = -1
    while queue:
        x, cnt = queue.popleft()
        if 0 <= x+1 <= 200000 and cnt+1 < visit[x+1]:
            visit[x+1] = cnt+1
            queue.append((x+1, cnt+1))
        if 0 <= x-1 <= 200000 and cnt+1 < visit[x-1]:
            visit[x-1] = cnt+1
            queue.append((x-1, cnt+1))
        if 0 <= 2*x <= 200000 and cnt < visit[2*x]:
            visit[2*x] = cnt
            queue.append((2*x, cnt))
    res = visit[k]
print(res)