def bfs(start, end):
    queue = [start]
    visited = [False for i in range(max(vtoe)+1)]
    cnt = 0
    while queue:
        nexts = []
        for i in queue:
            nexts.extend(roads[i])
            visited[i] = True
            if end in nexts:
                return cnt + 1
        k = 0
        for n in nexts:
            if visited[n] == True:
                k += 1
        if k == len(nexts):
            return 0
        queue = nexts
        cnt += 1
            

T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    vtoe = []
    for i in range(E):
        vtoe += list(map(int, input().split()))
    roads = [[] for _ in range(max(vtoe)+1)]
    for i in range(0, len(vtoe), 2):
        roads[vtoe[i]].append(vtoe[i+1])
        roads[vtoe[i+1]].append(vtoe[i])
    start, end = map(int, input().split())
    res = bfs(start, end)
    print('#{} {}'.format(t+1, res))
