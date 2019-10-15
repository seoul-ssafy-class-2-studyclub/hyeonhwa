# Kruskal's Algorithm
parent = {}
rank = {}

# 정점을 독립적인 집합으로 만듦
def make_set(v):
    parent[v] = v
    rank[v] = 0

# 해당 정점의 최상위 정점을 찾음
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

# 두 정점 연결
def union(v, u):
    root1 = find(v)
    root2 = find(u)
    if root1 != root2:
        if rank[root1] > rank[root2]: # 짧은 트리 -> 긴 트리 가리키게 함
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal():
    for v in range(V+1):
        make_set(v)
    mst = 0
    for v, u, w in nodes:
        if find(v) != find(u):
            union(v, u)
            mst += w
    return mst


T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(E)]
    nodes.sort(key=lambda x:x[2])
    res = kruskal()
    print('#{} {}'.format(t+1, res))
