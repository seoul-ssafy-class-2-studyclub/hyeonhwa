import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

def solve(x):
    res = [0]*(n+1)
    pq = []
    heapq.heappush(pq, x)
    while pq:
        loc = heapq.heappop(pq)
        for nxt, l in length[loc].items():
            if res[nxt]:
                continue
            nxt_l = res[loc] + l
            if nxt_l > res[nxt]:
                res[nxt] = nxt_l
                heapq.heappush(pq, nxt)
    return (max(res), res.index(max(res)))


n = int(input())
length = [{} for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    if length[a].get(b):
        length[a][b] = max(length[a][b], c)
    else:
        length[a][b] = c
    if length[b].get(a):
        length[b][a] = max(length[b][a], c)
    else:
        length[b][a] = c
ans, idx = solve(1)
ans, idx = solve(idx)
print(ans)