import heapq

def go(s):
    queue = []
    heapq.heappush(queue, (0, s))
    distance = [1e10]*(n+1)
    distance[s] = 0
    while queue:
        value, node = heapq.heappop(queue)
        for nd in nodes[node]:
            if value + 1 < distance[nd]:
                distance[nd] = value + 1
                heapq.heappush(queue, (value+1, nd))
    res = []
    for i in range(1, len(distance)):
        if distance[i] == k:
            res.append(i)
    return res

n, m, k, x = map(int, input().split())
nodes = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
res = go(x)
if not res:
    print(-1)
else:
    res.sort()
    print('\n'.join(list(map(str, res))))
