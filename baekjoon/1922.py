import heapq

N = int(input())
M = int(input())
computers = [[] for _ in range(N+1)]
INF = float('inf')
for _ in range(M):
    a, b, c = map(int, input().split())
    computers[a].append((b, c))
    computers[b].append((a, c))
visit = [False]*(N+1)
cost = [INF]*(N+1)
cost[1] = 0
queue = []
heapq.heappush(queue, (0, 1))
while queue:
    value, node = heapq.heappop(queue)
    visit[node] = True
    for n, v in computers[node]:
        if visit[n]:
            continue
        if cost[n] > v:
            cost[n] = v
            heapq.heappush(queue, (v, n))
# print(cost)
print(sum(cost[1:]))
