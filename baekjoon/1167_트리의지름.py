import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

def solve(x):
    res = [0]*(n+1)
    pq = []
    heapq.heappush(pq, x)
    while pq:
        loc = heapq.heappop(pq)
        for nxt, l in nodes[loc].items():
            if res[nxt] or nxt == x:
                continue
            length = l + res[loc] 
            if length > res[nxt]:
                heapq.heappush(pq, nxt)
                res[nxt] = length
    return max(res), res.index(max(res))

n = int(input())
nodes = [{} for _ in range(n+1)]
for _ in range(n):
    arr = [int(i) for i in input().split()]
    a = arr[0]
    arr = arr[1:-1]
    for i in range(0, len(arr), 2):
        b = arr[i]
        c = arr[i+1]
        if nodes[a].get(b):
            nodes[a][b] = max(nodes[a][b], c)
        else:
            nodes[a][b] = c
ans, i = solve(1)
print(solve(i)[0])