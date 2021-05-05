import heapq

n = int(input())
m = int(input())
bus_info = [{} for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if bus_info[a].get(b):
        bus_info[a][b].append(c)
    else:
        bus_info[a][b] = [c]
s, e = map(int, input().split())
INF = float('INF')
cost = [INF]*(n+1)
cost[s] = 0
queue = []
heapq.heappush(queue, (0, s))
while queue:
    value, node = heapq.heappop(queue)
    for nxt_node, nxt_value in bus_info[node].items():
        for nxt in nxt_value:
            if nxt + value < cost[nxt_node]:
                cost[nxt_node] = nxt + value
                heapq.heappush(queue, (cost[nxt_node], nxt_node))
print(cost[e])
