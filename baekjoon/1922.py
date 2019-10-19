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

# parent = [i for i in range(N+1)]
# rank = [0]*(N+1)

# def find(v):
#     if parent[v] != v:
#         parent[v] = find(parent[v])
#     return parent[v]

# def union(v, u):
#     root1 = find(v)
#     root2 = find(u)
#     if root1 != root2:
#         if rank[root1] > rank[root2]:
#             parent[root2] = root1
#         else:
#             parent[root1] = root2
#             if rank[root1] == rank[root2]:
#                 rank[root2] += 1


# def kruskal():
#     mst = 0
#     for v, u, c in nodes:
#         if find(v) != find(u):
#             union(v, u)
#             mst += c
#     return mst