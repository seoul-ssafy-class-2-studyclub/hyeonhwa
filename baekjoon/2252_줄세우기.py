from collections import deque

def tsort():
    result = []
    queue = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
    for _ in range(N):
        if not queue:
            return 0
        x = queue.popleft()
        result.append(x)
        for node in nodes[x]:
            indegree[node] -= 1
            if indegree[node] == 0:
                queue.append(node)
    return result


N, M = map(int, input().split())
nodes = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    indegree[b] += 1
res = tsort()
print(' '.join(list(map(str, res))))
