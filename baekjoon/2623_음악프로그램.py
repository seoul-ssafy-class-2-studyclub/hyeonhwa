import collections

# nodelist
def make(u, v):
    if v not in node[u]:
        node[u].append(v)
        indegree[v] += 1


def topologicalSort():
    queue = collections.deque()
    result = []
    for v in range(1, N+1):
        if indegree[v] == 0:
            queue.append(v)
        
    for _ in range(N):
        if not queue:
            return [0]
        x = queue.popleft()
        result.append(x)
        for nxt in node[x]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return result            


N, M = map(int, input().split())
# 위에 있어야 하는 node를 나타냄
node = [[] for _ in range(N+1)]
# 위에 몇개가 있어야하는지 나타냄
indegree = [0] * (N+1)
for _ in range(M):
    nodes = list(map(int, input().split()))
    for i in range(1, nodes[0]+1):
        for j in range(i+1, nodes[0]+1):
            make(nodes[i], nodes[j])
for i in topologicalSort():
    print(i)
