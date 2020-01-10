import sys
from heapq import heappop, heappush
input = lambda: sys.stdin.readline().rstrip()

def mst():
    m = [0]*(N+1)
    visit = [False]*(N+1)
    pqueue = []
    heappush(pqueue, (-1e9, s))
    visit[s] = True
    m[s] = 1e9
    while pqueue:
        value, node = heappop(pqueue)
        visit[node] = True
        value = -value
        for nxt, nvalue in bridge[node].items():
            if visit[nxt]:
                continue
            if min(value, nvalue) > m[nxt]:
                m[nxt] = min(value, nvalue)
                heappush(pqueue, (-min(value, nvalue), nxt))
    return m[e]

N, M = map(int, input().split())
bridge = [{} for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    if not bridge[a].get(b):
        bridge[a][b] = c
    else:
        bridge[a][b] = max(bridge[a][b], c)
    if not bridge[b].get(a):
        bridge[b][a] = c
    else:
        bridge[b][a] = max(bridge[b][a], c)
s, e = map(int, input().split())
# print(bridge)
res = mst()
print(res)

'''
9 9
1 4 11
1 5 2
4 5 4
4 3 10
4 2 7
5 2 10
5 6 13
3 2 9
2 6 8
1 6

9
'''