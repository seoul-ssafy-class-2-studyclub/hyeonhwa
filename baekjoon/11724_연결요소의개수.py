n, m = map(int, input().split())
nodes = [[] for _ in range(n+1)]
check = [0]*(n+1)
for __ in range(m):
    u, v = map(int, input().split())
    nodes[u].append(v)
    nodes[v].append(u)
connected = 0
queue = []
for i in range(1, n+1):
    if not check[i]:
        queue.append(i)
        check[i] = 1
        connected += 1
    while queue:
        x = queue.pop()
        for j in nodes[x]:
            if not check[j]:
                check[j] = 1
                queue.append(j)
print(connected)