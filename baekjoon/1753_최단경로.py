import heapq

v, e = map(int, input().split())
k = int(input())
nodes = [{} for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    if nodes[a].get(b):
        nodes[a][b] = min(nodes[a][b], c)
    else:
        nodes[a][b] = c
queue = []
cost = [1e10]*(v+1)
cost[k] = 0
heapq.heappush(queue, (0, k))
while queue:
    value, node = heapq.heappop(queue)
    for nxt_node, nxt_value in nodes[node].items():
        if nxt_value + value < cost[nxt_node]:
            cost[nxt_node] = nxt_value+value
            heapq.heappush(queue, (cost[nxt_node], nxt_node))
for i in range(1, v+1):
    if cost[i] == 1e10:
        print('INF')
    else:
        print(cost[i])
