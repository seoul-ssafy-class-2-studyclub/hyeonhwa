# import sys
# sys.stdin = open('1219.txt', 'r')

def dfs(visited, graph):
    stack = []
    stack.append(0)
    while stack:
        node = stack.pop()
        if visited[99]:
            return 1
        if not visited[node]:
            visited[node] = True
            stack.extend(graph[node])
        if 99 in stack:
            return 1
    if visited[99]:
        return 1
    else:
        return 0


for t in range(10):
    N, M = map(int, input().split())
    l = list(map(int, input().split()))
    graph = [[] for i in range(100)]
    visited = [False for i in range(100)]
    for i in range(0, len(l), 2):
        graph[l[i]] += [l[i+1]]
    print(f'#{t+1} {dfs(visited, graph)}')