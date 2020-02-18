def db():
    queue = [V]
    stack = [V]
    visit_d = [0]*(N+1)
    visit_b = [0]*(N+1)
    while queue:
        x = queue.pop(0)
        if visit_b[x] == 0:
            visit_b[x] = 1
            bfs.append(x)
            queue.extend(sorted(nodes[x]))
    while stack:
        x = stack.pop()
        if visit_d[x] == 0:
            visit_d[x] = 1
            dfs.append(x)
            stack.extend(sorted(nodes[x], reverse=True))


N, M, V = map(int, input().split())
nodes = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
dfs, bfs = [], []
db()
print(' '.join(list(map(str, dfs))) + '\n' + ' '.join(list(map(str, bfs))))