import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
if n == k:
    print(f'0\n{n}')
else:
    past = {}
    queue = deque()
    queue.append((n, 0))
    visit = [1e9 for _ in range(200001)]
    visit[n] = 0
    while queue:
        x, cnt = queue.popleft()
        if x == k:
            break
        if 0 <= x+1 <= 200000 and cnt+1 < visit[x+1]:
            visit[x+1] = cnt+1
            past[x+1] = x
            queue.append((x+1, cnt+1))
        if 0 <= x-1 <= 200000 and cnt+1 < visit[x-1]:
            visit[x-1] = cnt+1
            past[x-1] = x
            queue.append((x-1, cnt+1))
        if 0 <= 2*x <= 200000 and cnt < visit[2*x]:
            visit[2*x] = cnt
            past[2*x] = x
            queue.append((2*x, cnt))
    res = visit[k]
    key = k
    res = [key]
    while past.get(key) != None and key != n:
        res.insert(0, past[key])
        key = past[key]
    print(len(res)-1)
    print(' '.join(list(map(str, res))))