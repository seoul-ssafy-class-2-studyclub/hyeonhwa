# import sys
# sys.stdin = open('input.txt', 'r')

for t in range(10):
    V, E = map(int, input().split())
    e = list(map(int, input().split()))
    dfs = [0 for i in range(1, V+1)]
    visited = []
    graph = [[] for i in range(V)]
    s = set()
    for i in range(0, len(e), 2):
        graph[e[i]-1].append(e[i+1]) # [[2, 5], [3, 7], [], [1], [6], [], [6], [5, 9], []]
        dfs[e[i+1]-1] += 1
        s.update({e[i+1]})
        stack = {i for i in range(1, V+1)}.difference(s)
    stack = list(stack)
    while stack:
        node = stack.pop()
        if dfs[node-1]:
            dfs[node-1] -= 1
        if dfs[node-1] == 0:
            visited.append(node)
            stack.extend(graph[node-1])
    print('#{} {}'.format(t+1, ' '.join(list(map(str, visited)))))
