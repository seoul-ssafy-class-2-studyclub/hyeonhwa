def cnt():
    global res
    queue = nodes[N]
    while queue:
        x = queue.pop(0)
        if visit[x] == False:
            visit[x] = True
            res += 1
            queue.extend(nodes[x])


T = int(input())
for t in range(T):
    E, N = map(int, input().split())
    node = list(map(int, input().split()))
    nodes = [[] for _ in range(E+3)]
    visit = [False] * len(nodes)
    for i in range(0, len(node), 2):
        nodes[node[i]] += [node[i+1]]
    res = 1
    cnt()
    print('#{} {}'.format(t+1, res))